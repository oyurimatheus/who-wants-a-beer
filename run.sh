#!/bin/bash

export DATABASE_NAME=whowantsabeer
export DATABASE_USER=app
export DATABASE_PASSWORD=app
export DATABASE_HOST=172.16.1.2
export DEBUG=False

docker network create -d bridge --subnet 172.16.1.0/24 --gateway 172.16.1.1 beer-prod
docker container run -e POSTGRES_USER=app -e POSTGRES_PASSWORD=app -e POSTGRES_DB=whowantsabeer --net=beer-prod --name whowantsabeer -d mdillon/postgis
sleep 10
python -m src.infra.create_db
docker container run -p 5000:5000 --net=beer-prod --name beer-app -d oyurimatheus/whowantsabeer