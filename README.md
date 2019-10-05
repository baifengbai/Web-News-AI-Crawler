# Web-News-AI-Crawler
This is a web crawler which uses AI to filter most interesting news from the internet 

### Installation
1. Install MondgoDB and create database:

```console
docker run -d --restart=unless-stopped --name rpi3-mongodb3 --restart unless-stopped -v /home/pi/volume/mongodb/db:/data/db -v /home/pi/volume/mongodb/configdb:/data/configdb -p 27017:27017 -p 28017:28017 andresvidal/rpi3-mongodb3:latest mongod --auth 

docker exec -it rpi3-mongodb3 mongo admin

db.createUser(
  {
    user: "rio",
    pwd: "onslario89",
    roles: [ { role: "readWrite", db: "rss_news" } ]
  }
)

db.auth("<user>", "<psw>")

```

2. Install cronjobs

3. pip3 install -r requierements.txt

4. Put writer and reader scripts into /home/pi/Scripts/

5. sudo apt-get install libatlas-base-dev

6. Start backend server: nohup python3 /home/pi/Scripts/backend/api-server.py &
