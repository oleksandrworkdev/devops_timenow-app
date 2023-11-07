#! /bin/bash
sudo openssl req -nodes -days 365 -newkey rsa:2048 `
-keyout /etc/ssl/private/nginx-selfsigned.key `
-out /etc/ssl/certs/nginx-selfsigned.crt