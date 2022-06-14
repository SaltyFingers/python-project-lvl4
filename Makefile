run:
	poetry run python3 manage.py runserver

lint:
	poetry run flake8 task_manager
locale:
	poetry run django-admin makemessages -l ru

compile:
	poetry run django-admin compilemessages


