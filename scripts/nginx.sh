#!/usr/bin/bash

sudo systemctl daemon-reload
systemctl restart gunicorn.service
sudo cp /home/ubuntu/django-aws_cicd/nginx/nginx.conf /etc/nginx/sites-available/django-aws_cicd
sudo ln -s /etc/nginx/sites-available/django-aws_cicd /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
sudo ufw delete allow 8000
sudo ufw allow 'Nginx Full'