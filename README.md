# django project setup
## vitural enviroment
cd project_folder
python3 -m venv env
source env/bin/activate
## install packages 
cd project_folder/src
pip install -r ../requirements.txt
## create file .env (path: project_folder/src/src/.env)
SECRET_KEY=

DB_ENGINE=django.db.backends.mysql # change engine if need
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

## generate secret key
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())

## run project 
cd project_folder/src
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


