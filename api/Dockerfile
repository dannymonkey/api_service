FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["python3"]
CMD ["app.py", "--port", "5001"]
