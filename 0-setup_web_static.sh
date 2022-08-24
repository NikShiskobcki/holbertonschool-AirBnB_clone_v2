#!/usr/bin/env bash
# setting up web servers for the deployment of web_static

#installs nginx
sudo su
apt-get update -y
apt-get install nginx -y

#creates directories needed
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# fake html
printf %s "<html>
    <head>
    </head>
    <body>
        test html
    </body
</html>" > /data/web_static/releases/test/index.html

#creating symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current/

# give ownership to user and group
chown -R ubuntu /data/
chgrp -R ubuntu /data

#update nginx configuration
sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}" \etc/nginx/sites-available/default

sudo service nginx start
