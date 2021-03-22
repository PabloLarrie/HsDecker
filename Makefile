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
	
freeze_dependencies: pip_compile chown

run:
	${DOCKER_HSDECKER} python manage.py runserver

loadcards:
	${DOCKER_HSDECKER} python manage.py loaddata cards/fixtures/*

loaddecks:
	${DOCKER_HSDECKER} python manage.py loaddata decks/fixtures/*

loaddata:loadcards loaddecks

migrate:
	${DOCKER_HSDECKER} python manage.py migrate

makemigrations:
	${DOCKER_HSDECKER} python manage.py makemigrations