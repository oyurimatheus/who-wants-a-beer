from sqlalchemy import create_engine, MetaData

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://app:app@172.16.0.2:5432/whowantsabeer')
meta_data = MetaData(bind=engine)

session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = scoped_session(session_factory)

Base = declarative_base(bind=engine, metadata=meta_data)
Base.query = db_session.query_property()
