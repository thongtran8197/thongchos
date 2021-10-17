----- django project setup -----
1. 
cd project_folder
python3 -m venv env
source env/bin/activate
2. install packages 
cd project_folder/src
pip install -r ../requirements.txt
3. create file .env (path: project_folder/src/src/.env)
# Secret Key
SECRET_KEY=

# DB setting
DB_ENGINE=django.db.backends.mysql # change engine if need
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

4. generate secret key
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())

5. run project 
cd project_folder/src
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


