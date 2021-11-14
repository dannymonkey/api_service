from argparse import ArgumentParser
import base64
import datetime
import psycopg2
import pickle

from flask import Flask
from flask import request
from flask import jsonify
import numpy as np
import pandas as pd


app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))

####### PUT YOUR INFORMATION HERE #######
CAPTAIN_EMAIL = 'my@gmail.com'          #
server_uuid = 'testing'                 #
#########################################


def test_predict(image):
    """ Predict your model result.

    @param:
        image (numpy.ndarray): an image.
    @returns:
        prediction (str): a word.
    """

    ####### PUT YOUR MODEL INFERENCING CODE HERE #######
    prediction = '陳'


    ####################################################
    if _check_datatype_to_string(prediction):
        return prediction


def _check_datatype_to_string(prediction):
    """ Check if your prediction is in str type or not.
        If not, then raise error.

    @param:
        prediction: your prediction
    @returns:
        True or raise TypeError.
    """
    if isinstance(prediction, str):
        return True
    raise TypeError('Prediction is not in string type.')

@app.route('/health', methods=['GET'])
def health_check():
    """ check API alive"""
    return "OK"

@app.route('/user_info', methods=['POST'])
def user_info():
    """ API that return the user info. """
    data = request.get_json(force=True)

    try:
        user_id = data['user_id']
    except Exception as e:
        print(e)
        raise e
    
    try:
        conn = psycopg2.connect(host="db",
                                database="postgres",
                                user="postgres",
                                password="postgres123")
    except Exception as e:
        print(e)
        raise e
    
    db_result = pd.read_sql("""select user_name, user_info
                                 from api_data;""", conn)
    
    return jsonify({'user_name':f'{db_result["user_name"][0]}',
                    'user_info':f'{db_result["user_info"][0]}'})


@app.route('/inference', methods=['POST'])
def inference():
    """ API that return your model predictions when somebody calls this API. """
    data = request.get_json(force=True)
    print('get requests')

    try:
        answer = test_predict("")
    except TypeError as type_error:
        # You can write some log...
        print(type_error)
        raise type_error
    except Exception as e:
        # You can write some log...
        print(e)
        raise e
    server_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return jsonify({'server_uuid': server_uuid,
                    'answer': answer,
                    'server_timestamp': server_timestamp})

@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([[np.array(data['exp'])]])
    # Take the first value of prediction
    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=8080, help='port')
    arg_parser.add_argument('-d', '--debug', default=True, help='debug')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port, host = "0.0.0.0")

