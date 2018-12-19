#!/bin/bash

docker network create -d bridge --subnet 172.16.0.0/24 --gateway 172.16.0.1 beer-dev
docker container run -e POSTGRES_USER=app -e POSTGRES_PASSWORD=app -e POSTGRES_DB=whowantsabeer --net=beer-dev -d mdillon/postgis
sleep 10
pip install -r requirements.txt
python -m src.infra.create_db
python -m tests.generate_db_data
python  server.py
