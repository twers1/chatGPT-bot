FROM python:3.10-alpine

ARG TOKEN
ARG OPENAI_API_KEY

ENV TOKEN=$TOKEN
ENV OPENAI_API_KEY=$OPENAI_API_KEY

WORKDIR /app

COPY requirements.txt requirements.txt
COPY main.py main.py

RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python", "main.py"]