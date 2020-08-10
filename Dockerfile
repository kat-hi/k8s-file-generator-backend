# server setup
FROM python:3.6

RUN mkdir app
# install requirements
COPY app/ app/

COPY requirements.txt app/
WORKDIR app

RUN chmod +x requirements.txt

RUN pip install -r requirements.txt --no-cache-dir --compile

ENV PYTHONUNBUFFERED=1

ENV FLASK_ENV=development

CMD flask run --host 0.0.0.0