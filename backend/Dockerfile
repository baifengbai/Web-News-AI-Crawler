FROM jiashenc/arm-keras

MAINTAINER Rio<onslaught89@gmail.com>

RUN mkdir /root/backend

COPY models /root/backend/

COPY api-server.py /root/backend/

RUN pip install Flask pandas

EXPOSE 5003/tcp

CMD [ "python", "/root/backend/api-server.py" ]
