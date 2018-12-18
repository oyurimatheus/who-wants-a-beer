dev:
	bash run-dev.sh

prod:
	bash run.sh

build:
	docker image build -f Dockerfile -t oyurimatheus/whowantsabeer .
	docker push oyurimatheus/whowantsabeer