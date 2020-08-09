# server setup
FROM python:3.6

# install requirements
COPY . .

RUN chmod +x requirements.txt

RUN pip install -r requirements.txt --no-cache-dir --compile

ENV PYTHONUNBUFFERED=1

EXPOSE 5005

CMD ["flask", "run", "--host","0.0.0.0", "--port", "5005"]