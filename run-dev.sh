docker network create -d bridge --subnet 172.16.0.0/24 --gateway 172.16.0.1 containers
docker container run -e POSTGRES_USER=app -e POSTGRES_PASSWORD=app -e POSTGRES_DB=whowantsabeers --net=containers --name whowantsabeer -d mdillon/postgis
python -m src.infra.create_db.py
python -m src.infra.server.py