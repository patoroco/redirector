.PHONY: start shell test deploy

start:
	python manage.py runserver

shell:
	python manage.py shell

test:
	python manage.py test

deploy:
	git push dokku
