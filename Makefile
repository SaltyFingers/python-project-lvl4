run:
	poetry run python3 manage.py runserver

test:
	poetry run python3 manage.py test

migrations:
	poetry run python3 manage.py makemigrations

migrate:
	poetry run python3 manage.py migrate

lint:
	poetry run flake8 task_manager

locale:
	poetry run python3 manage.py makemessages -l ru

compile:
	poetry run django-admin compilemessages
