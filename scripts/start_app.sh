#!/usr/bin/bash 

sed -i 's/\[]/\["18.210.11.217"]/' /home/ubuntu/django-aws_cicd/awscicd/settings.py
sudo systemctl restart gunicorn
sudo systemctl restart nginx
