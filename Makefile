ifdef DEVCONTAINER
	DOCKER_HSDECKER=
else
	DOCKER_HSDECKER=docker-compose run hsdecker
endif

build:
	docker-compose build

shell:
	${DOCKER_HSDECKER} python manage.py shell_plus

chown:
	sudo chown `whoami` -R .

pip-compile:
	${DOCKER_HSDECKER} pip-compile requirements.in > requirements.txt
	
freeze_dependencies: pip-compile chown

run:
	${DOCKER_HSDECKER} python manage.py runserver

loadusers:
	${DOCKER_HSDECKER} python manage.py loaddata hsdecker/fixtures/*

loadcards:
	${DOCKER_HSDECKER} python manage.py loaddata cards/fixtures/*

loaddecks:
	${DOCKER_HSDECKER} python manage.py loaddata decks/fixtures/*

loaddata: loadusers loadcards loaddecks

migrate:
	${DOCKER_HSDECKER} python manage.py migrate

makemigrations:
	${DOCKER_HSDECKER} python manage.py makemigrations