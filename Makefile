ifdef DEVCONTAINER
	DOCKER_HSDECKER=
else
	DOCKER_HSDECKER=docker-compose run hsdecker
endif

build:
	docker-compose build

# build_pro:
# 	docker-compose build \
#   	--build-arg USER_ID=`id -u` \
#   	--build-arg GROUP_ID=`id -g`

shell:
	${DOCKER_HSDECKER} python manage.py shell_plus

chown:
	sudo chown `whoami` -R .

pip-compile:
	${DOCKER_HSDECKER} pip-compile requirements.in > requirements.txt
	
freeze_dependencies: pip_compile chown

runserver:
	${DOCKER_HSDECKER} python manage.py runserver
