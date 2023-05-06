# UI Project for Mircobiome Analysis Platform

## Setup
### Local Development Setup
#### [Verify Python Version](https://www.python.org/downloads/)
```sh
python --version
```
**If above command does not return ```Python 3.9``` or greater, replace throughout this tutorial ```python3``` instead of ```python```**

#### [Install Django](https://docs.djangoproject.com/en/4.2/topics/install/)
```sh
python -m pip install Django
```
#### [Install Postgres](https://www.postgresql.org/download/)
```sh
brew install postgresql
```
#### [Install Redis](https://redis.io/docs/getting-started/installation/)
```sh
brew install redis
```

#### Clone Repository
```sh
git clone https://github.com/aikene/microbiome-project-ui.git
```
#### Create and Activate Virtual Environment
```sh
python -m venv env
```
```sh
source env/bin/activate
```
#### Install Dependencies
```shell
pip install -r requirements.txt
```
**update may be needed in requirements.txt file to update line 2 to:
```backports.zoneinfo==0.2.1;python_version<"3.9"```
#### Change settings.py
If no .env file was provided, 
Remove anywhere  ```env('VALUE')``` is and make sure your 'Databases' dictionary in awscid/settings.py is set to use a local database
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
#### Start Application
Run this command from main project level
```python
python manage.py runserver
```

GitHub branch -> AWS CodePipeline -> AWS CodeDeploy -> AWS Elastic Compute Cloud

## Original How-To Guide
[AWS CI-CD for your Django app with AWS CodePipeline](https://medium.com/clairvoyantblog/aws-ci-cd-for-your-django-app-with-aws-codepipeline-aafec23f9e55)
