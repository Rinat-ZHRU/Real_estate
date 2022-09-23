Проект: real_estate (Сайт для продажи недвижимости)

Реализация:
	Django Rest Framework
	База данных: PostreSQL

Ссылки на ГИТ:

	HTTPS:

	https://github.com/Rinat-ZHRU/Real_estate

	SSH key:

	git@github.com:Rinat-ZHRU/Real_estate.git

Развертывание проекта

Развернуть локально

	python3 -m venv venv
	source venv/bin/activate
	pip install -r req.txt
	python manage.py makemigrations
	python manage.py migrate
	
Установка пакетов

	pip install -r requirements.txt		

Развернуть через Docker

	docker-compose up -d --build
	docker-compose logs -f


ENV:

	SECRET_KEY=django-insecure-)y-t5eb3)0^t-a6)tm1v-&*n5r+9sfw*=bq!@bg*bguv^8!@1$
	DEBUG=1
	POSTGRES_ENGINE=django.db.backends.postgresql
	POSTGRES_DB=real_estate_db
	POSTGRES_USER=real_estate_user
	POSTGRES_PASSWORD=real estate
	POSTGRES_HOST=localhost
	POSTGRES_PORT=5432
