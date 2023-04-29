#!/usr/bin/bash 

sed -i 's/\[]/\["35.85.19.246"]/' /home/ubuntu/django-aws_cicd/awscicd/settings.py
sudo systemctl restart gunicorn
sudo systemctl restart nginx