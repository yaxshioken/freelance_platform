sort:
	black .
	isort .
mig:
	python3 manage.py makemigrations
	python3 manage.py migrate