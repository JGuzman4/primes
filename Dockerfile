FROM python:3.11.9-alpine3.19

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY main.py main.py

ENTRYPOINT [ "python3", "main.py" ]
