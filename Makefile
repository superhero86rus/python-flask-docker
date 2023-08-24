APP_NAME = python-flask-docker
APP_FULL_NAME = ${APP_NAME}:latest
IMAGE_NAME = superhero86/${APP_FULL_NAME}

run:
	docker run --rm -d -v `pwd`:/app -p 5000:5000 -v logs:/app/logs --name ${APP_NAME} ${IMAGE_NAME}
stop:
	docker stop ${APP_NAME}
rmc:
	docker rm ${APP_NAME}
rmi:
	docker rmi ${IMAGE_NAME}
build:
	docker build -t ${IMAGE_NAME} .
push:
	docker push ${IMAGE_NAME}