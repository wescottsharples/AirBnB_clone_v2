#!/usr/bin/env bash
# Bash script sets u pweb servers for deployment.

FILE=/etc/nginx/sites-available/default
REDIRECT="location /hbnb_static {\n alias /data/web_static/current; \n}\n"

sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "<h1>Wassup</h1>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i "35i $REDIRECT" $FILE
sudo service nginx restart
