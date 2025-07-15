run:
	@python3 manage.py runserver

db:
	@python3 manage.py makemigrations
	@python3 manage.py migrate

requirements:
	@pip freeze > requirements.txt

createsuperuser:
	@python3 manage.py createsuperuser

test:
	@python3 manage.py test
