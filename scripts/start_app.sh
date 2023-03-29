#!/usr/bin/bash 

sed -i 's/\[]/\["54.237.113.155"]/' /home/ubuntu/django-aws_cicd/awscicd/settings.py
sudo systemctl restart gunicorn
sudo systemctl restart nginx
