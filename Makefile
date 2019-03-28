.PHONY: start

start:
	workon redirector
	python manage.py runserver

deploy:
	git push dokku
