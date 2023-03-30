#!/usr/bin/bash 

sed -i 's/\[]/\["52.43.192.160"]/' /home/ubuntu/django-aws_cicd/awscicd/settings.py
sudo systemctl restart gunicorn
sudo systemctl restart nginx