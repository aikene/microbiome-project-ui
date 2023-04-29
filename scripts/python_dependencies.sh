#!/usr/bin/env bash

virtualenv /home/ubuntu/env
source /home/ubuntu/env/bin/activate
pip install -r /home/ubuntu/django-aws_cicd/requirements.txt

cp /home/ubuntu/.env /home/ubuntu/django-aws_cicd/awscicd/.env
cd /home/ubuntu/django-aws_cicd/
python3 manage.py collectstatic --noinput