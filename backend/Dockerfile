FROM arm32v7/python:latest

MAINTAINER Rio<onslaught89@gmail.com>

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    build-essential \
    ca-certificates \
    gcc \
    git \
    libpq-dev \
    make \
    python-pip \
    python3-dev \
    ssh \
    libatlas-base-dev \
    libhdf5-dev python-h5py \
    && apt-get autoremove \
    && apt-get clean

RUN mkdir $HOME/scripts

RUN cp ./* $HOME/scripts

RUN pip install --upgrade pip 

RUN pip install feedparser pymongo pandas flask numpy tensorflow keras==2.2.4 h5py 

EXPOSE 5000/tcp

CMD [ "python3", "/home/root/scripts/backend/api-server.py" ]
