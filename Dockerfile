FROM python:3.6

WORKDIR /code

EXPOSE 5000

ADD requirements.txt ./
ADD run.sh ./
ADD ./server.py ./ 

RUN pip install -r requirements.txt
RUN mkdir src/
RUN touch ./src/__init__.py
COPY src ./src

ENTRYPOINT python server.py