FROM python:3.10
RUN apt update && apt upgrade -y
RUN apt install python3-pip -y
RUN apt install ffmpeg -y
RUN apt-get install -y nodejs
RUN npm i -g npm
RUN mkdir /app/
COPY . /app
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
CMD python3 main.py
FROM nikolaik/python-nodejs:python3.10-nodejs19
