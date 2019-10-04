# Web-News-AI-Crawler
This is a web crawler which uses AI to filter most interesting news from the internet 

### Installation
1. Install MondgoDB and create database:

```console
docker run -d --restart=unless-stopped --name rpi3-mongodb3 --restart unless-stopped -v /home/pi/volume/mongodb/db:/data/db -v /home/pi/volume/mongodb/configdb:/data/configdb -p 27017:27017 -p 28017:28017 andresvidal/rpi3-mongodb3:latest mongod --auth 

docker exec -it rpi3-mongodb3 mongo admin

db.createUser({ user: "<user>", pwd: "<psw>", roles: [ { role: "userAdminAnyDatabase", db: "admin" } ] })

db.auth("<user>", "<psw>")

use rss_news
```

2. Install cronjobs

3. Put writer and reader scripts into /home/pi/Scripts/

4. Start backend server (/backend/api-server.py)