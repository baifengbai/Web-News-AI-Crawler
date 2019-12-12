# Web-News-AI-Crawler
This is a web crawler which uses AI to filter most interesting news from the internet 

### Run:

from ARM (i.e. RaspberryPi):

```console
docker run -it --rm --name = ai_news -e TELEGRAM_BOT_TOKEN = '<token>' -e TELEGRAM_CHAT_ID='<id>' rio05docker/ai_news_server:rpi3_develop_07a96d304c5b08c16b025d21ba51c60b53d1a91b
```

from x86:

```console
docker run -it --rm -v /usr/bin/qemu-arm-static:/usr/bin/qemu-arm-static --name = ai_news -e TELEGRAM_BOT_TOKEN = '<token>' -e TELEGRAM_CHAT_ID='<id>' rio05docker/ai_news_server:rpi3_develop_07a96d304c5b08c16b025d21ba51c60b53d1a91b
```
