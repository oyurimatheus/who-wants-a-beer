dev:
	bash run-dev.sh

prod:
	docker-compose up

build:
	docker image build -f Dockerfile -t oyurimatheus/whowantsabeer .
	docker push oyurimatheus/whowa  ntsabeer