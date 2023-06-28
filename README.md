# ChatGPT 

is a bot that accepts a user's requests and throws him an answer 

## How to install? 

```commandline

pip install -r requirements.txt

python3 main.py
```

## Demo

![](https://github.com/twers1/chatGPT-bot/blob/main/gif/demogpt.gif)

## Docker documentation. Getting Started

Dockerfile: 

FROM python:3.11.1-slim-buster as builder - let's state that our application is based on Python version 3.10.

WORKDIR /app - We will immediately mark the directory in which we are going to work. This is just a folder inside absolutely any image

Commands: 

- docker build -t bot . - for the build in docker. Instead of bot it can be any other name, because we create a new image
- docker run -e TOKEN= -e OPENAI_API_KEY= bot - running a project in docker
-  docker-compose up - creates a ready container (with database, redis and the bot itself)


# ChatGPT

это бот, который принимает запросы пользователя и кидает ему ответ 

## Как установить?

```commandline

pip install -r requirements.txt

python3 main.py
```

## Демонстрация 

![](https://github.com/twers1/chatGPT-bot/blob/main/gif/demogpt.gif)


## Документация по Docker. Начало работы

Dockerfile:

FROM python:3.11.1-slim-buster as builder - заявим, что наше приложение основывается на питоне версии 3.10. 

WORKDIR /app - сразу же отметим директорию в которой будем работать. Это просто папка внутри абсолютно любого образа


Команды: 

- docker build -t bot . - для билда в docker. Вместо bot может быть любое другое название, так как мы создаем новый image
- docker run -e TOKEN= -e OPENAI_API_KEY= bot - запуск проекта в docker
- docker-compose up - создает готовый контейнер(с БД, redis и самим ботом)