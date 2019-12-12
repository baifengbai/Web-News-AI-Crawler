FROM derekmerck/keras-tfkeras-tf:py3-tf190-k222-arm32v7

RUN pip3 install telepot 
RUN pip3 install requests
RUN pip3 install feedparser
RUN pip3 install subprocess

RUN mkdir /home/scripts
RUN mkdir /home/scripts/models
WORKDIR /home/scripts
COPY ./models/rss_model.h5 /home/scripts/models
COPY ./feed_list.txt /home/scripts/
COPY ./stateless_news_ai.py /home/scripts

CMD ["python3", "stateless_news_ai.py"]