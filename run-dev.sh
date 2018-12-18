docker network create -d bridge --subnet 172.16.0.0/24 --gateway 172.16.0.1 beer
docker container run -e POSTGRES_USER=app -e POSTGRES_PASSWORD=app -e POSTGRES_DB=whowantsabeer --net=beer --name whowantsabeer -d mdillon/postgis
sleep 10
python -m src.infra.create_db
python -m tests.generate_db_data
python  server.py
