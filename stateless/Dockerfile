FROM derekmerck/keras-tf:py3-tf190-k222-arm32v7

RUN pip3 install telepot
RUN pip3 install requests
RUN pip3 install feedparser
#RUN pip3 install subprocess
#RUN pip3 install pandas
RUN pip3 install keras==2.2.4

RUN pip3 uninstall conda -y
RUN pip3 uninstall Pillow -y
RUN pip3 uninstall Werkzeug -y 

RUN mkdir /home/scripts
RUN mkdir /home/scripts/models
WORKDIR /home/scripts

COPY ./models/rss_model.h5 /home/scripts/models
COPY ./feed_list.txt /home/scripts/
COPY ./stateless_news_ai.py /home/scripts

CMD ["python3", "stateless_news_ai.py"]