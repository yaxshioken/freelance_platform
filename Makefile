sort:
	black .
	isort .
mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
user:
	python3 manage.py createsuperuser --phone +998940021444 --email superuser@test.com
