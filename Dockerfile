FROM python:3.6

WORKDIR /code

ADD requirements.txt ./
ADD run.sh ./

RUN pip install -r requirements.txt

ADD ./src /code

CMD ["./run.sh"]