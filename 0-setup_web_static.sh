#!/usr/bin/env bash
# Bash script sets u pweb servers for deployment.

#sudo apt-get -y update
#sudo apt-get -y install nginx

mkdir -p "/data/web_static/releases/test/"
mkdir -p "/data/web_static/shared/"
echo "<h1>Wassup</h1>" > "/data/web_static/releases/test/index.html"
ln -sf "/data/web_static/current" "/data/web_static/releases/test/"
chown -R ubuntu:ubuntu /data/
