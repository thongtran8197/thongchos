# django project setup
## vitural enviroment
cd project_folder <br />
python3 -m venv env <br />
source env/bin/activate <br />
## install packages 
cd project_folder/src <br />
pip install -r ../requirements.txt <br />
## create file .env (path: project_folder/src/src/.env)
SECRET_KEY= <br />

DB_ENGINE=django.db.backends.mysql # change engine if need <br />
DB_NAME= <br />
DB_USER= <br />
DB_PASSWORD= <br />
DB_HOST= <br />
DB_PORT= <br />

## generate secret key
from django.core.management.utils import get_random_secret_key <br />
print(get_random_secret_key()) <br />

## run project 
cd project_folder/src <br />
python manage.py makemigrations <br />
python manage.py migrate <br />
python manage.py createsuperuser <br />
python manage.py runserver <br />
