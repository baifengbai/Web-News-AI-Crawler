# Web-News-AI-Crawler
This is a web crawler which uses AI to filter most interesting news from the internet 

### Run:

from ARM (i.e. RaspberryPi):

```console
docker run -it --rm --name = ai_news -e TELEGRAM_BOT_TOKEN = '<token>' -e TELEGRAM_CHAT_ID='<id>' rio05docker/ai_news_server:rpi3_develop_89714b6a3deaedd9672f73525ccc435cac5cd9ee
```

from x86:

```console
docker run -it --rm -v /usr/bin/qemu-arm-static:/usr/bin/qemu-arm-static --name = ai_news -e TELEGRAM_BOT_TOKEN = '<token>' -e TELEGRAM_CHAT_ID='<id>' rio05docker/ai_news_server:rpi3_develop_89714b6a3deaedd9672f73525ccc435cac5cd9ee
```
