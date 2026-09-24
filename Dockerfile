FROM python:3.14.7-alpine3.24

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x run.sh

CMD ["./run.sh"]
