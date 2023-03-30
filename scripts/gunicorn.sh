#!/usr/bin/bash

sudo cp /home/ubuntu/django-aws_cicd/gunicorn/gunicorn.service  /etc/systemd/system/gunicorn.service
sudo systemctl start gunicorn
sudo systemctl enable gunicorn