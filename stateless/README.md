# Web-News-AI-Crawler
This is a web crawler which uses AI to filter most interesting news from the internet 

### Run:

```console
docker run -it --rm --name = ai_news -e TELEGRAM_BOT_TOKEN = '<token>' -e TELEGRAM_CHAT_ID='<id>' rio05docker/ai_news_server:rpi3_test_9
```