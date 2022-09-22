PROJECT'S NAME: real_estate (Сайт для продажи недвижимости)

CLONING PROJECT

for HTTPS:

https://github.com/Rinat-ZHRU/Real_estate

for SSH key:

git@github.com:Rinat-ZHRU/Real_estate.git

NEXT STEPS:

1.Install venv in project:

python3 -m venv venv 

2.Start virtualenv:

source venv/bin/activate

3.Installing all requirements:

pip install -r requirements.txt

TO START PROJECT:

1)sudo su (+ your password)

2)docker-compose up --build(to building docker and run server)

3)In another terminal:  docker-compose exec web python manage.py migrate --noinput

4)go to your browser and write in the search bar: 127.0.0.1:8000 or localhost:8000

IF YOU NEED TO GO IN DJANGO ADMIN PANEL AND YOU NEED TO CREATE SUPERUSER(ADMIN): 
(127.0.0.1:8000/admin/) or (localhost:8000)

1.In terminal:

docker ps -a


AND WRITE THIS FOR CREATING SUPERUSER(ADMIN):

python manage.py createsuperuser

ANYTHING URLS YOU HAVE IN DIR "real_estate_app", FILE "urls.py"

TESTS: DIR "real_estate_app", FILE "tests.py"

FOR TESTING TESTS, YOU NEED TO SWITCH DATABASE "postgres" TO "sqlite3" BY COMMENTING 
IN DIR "real_estate_app", FILE "settings.py"

NEED TO ADD ENV VARS:

SECRET_KEY=django-insecure-)y-t5eb3)0^t-a6)tm1v-&*n5r+9sfw*=bq!@bg*bguv^8!@1$
DEBUG=1
POSTGRES_ENGINE=django.db.backends.postgresql
POSTGRES_DB=real_estate_db
POSTGRES_USER=real_estate_user
POSTGRES_PASSWORD=real estate
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
