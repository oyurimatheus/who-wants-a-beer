# Who wants a beer?
Projeto que acha o ponto de venda mais próximo a residência de uma pessoa.

## Tecnologias usadas

* Python (3.6)
* pip
* GraphQl
* Postgres com Postgis
* Docker
* Pytest

## Rodando localmente
Para rodar a aplicação localmente, você precisa ter o Python na versão 3.6 e o `pip` instalados.

Basta digitar, na pasta do projeto, o comando `make dev`. 


## Buildando a imagem
Para criar uma imagem do Docker, basta digitar `make build` que a imagem é criada e enviada para o docker hub

## Rodando em produção

Basta rodar o comando `make prod` que será executado o `docker-compose` para subir a imagem.
