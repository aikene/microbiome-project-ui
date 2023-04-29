#!/usr/bin/env bash

virtualenv /home/ubuntu/env
source /home/ubuntu/env/bin/activate
pip install -r /home/ubuntu/django-aws_cicd/requirements.txt
cd /home/ubuntu/django-aws_cicd/
python3 manage.py collectstatic --noinput