ifdef DEVCONTAINER
	DOCKER_HSDECKER=
else
	DOCKER_HSDECKER=docker-compose run hsdecker
endif

ifdef DEVCONTAINER
	DOCKER_FRONTEND=
else
	DOCKER_FRONTEND=docker-compose run frontend
endif

test:
	${DOCKER_HSDECKER} pytest -c pytest.ini

pip-compile:
	${DOCKER_HSDECKER} pip-compile requirements.in > requirements.txt

shell:
	${DOCKER_HSDECKER} python manage.py shell_plus

chown:
	sudo chown `whoami` -R .

freeze_dependencies: pip-compile chown

run:
	${DOCKER_HSDECKER} python manage.py runserver

build:
	docker-compose build

migrate:
	${DOCKER_HSDECKER} python manage.py migrate

makemigrations:
	${DOCKER_HSDECKER} python manage.py makemigrations

loadcards:
	${DOCKER_HSDECKER} python manage.py loaddata cards/fixtures/*

loaddecks:
	${DOCKER_HSDECKER} python manage.py loaddata decks/fixtures/*

loadgroups:
	${DOCKER_HSDECKER} python manage.py setup_user_permissions

loadusers:
	${DOCKER_HSDECKER} python manage.py setup_user_creation

installfrontend:
	${DOCKER_FRONTEND} npm install

installvuestrap:
	${DOCKER_FRONTEND} npm install vue bootstrap bootstrap-vue

addvuestrap:
	${DOCKER_FRONTEND} vue add bootstrap-vue

installrouter:
	${DOCKER_FRONTEND} npm install vue-router

vuestrap: installvuestrap addvuestrap

build_and_setup: build migrate loadgroups loadusers loadcards loaddecks installfrontend
