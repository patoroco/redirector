.PHONY: start

start:
	python manage.py runserver

deploy:
	git push dokku
