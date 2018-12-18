docker run -e POSTGRES_USER=app -e POSTGRES_PASSWORD=app -e POSTGRES_DB=whowantsabeer --name whowantsabeer -d mdillon/postgis
python -m src.infra.create_db.py
python -m src.infra.server.py