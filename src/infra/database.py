from sqlalchemy import create_engine, MetaData

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

import os


DATABASE_USER = os.getenv('DATABASE_USER', 'app')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'app')
DATABASE_HOST = os.getenv('DATABASE_HOST', '127.0.0.1')
DATABASE_PORT = os.getenv('DATABASE_PORT', '5432')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'whowantsabeer')

url = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'
engine = create_engine(url)
meta_data = MetaData(bind=engine)

session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = scoped_session(session_factory)

Base = declarative_base(bind=engine, metadata=meta_data)
Base.query = db_session.query_property()
