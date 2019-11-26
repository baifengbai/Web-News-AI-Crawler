FROM arm32v7/ubuntu:16.04

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
    python3 \
    python3-dev \
    ssh \
    libatlas-base-dev \
    libhdf5-dev python-h5py \
    && apt-get autoremove \
    && apt-get clean

RUN mkdir $HOME/scripts

COPY ./* /home/root/scripts/

RUN pip install --upgrade && pip install -r /home/root/scripts/requierements.txt

EXPOSE 5000/tcp

CMD [ "python3", "/home/root/scripts/backend/api-server.py" ]