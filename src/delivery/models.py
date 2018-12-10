from sqlalchemy import Column
from sqlalchemy import Integer, String
from geoalchemy2 import Geometry


from src.infra.database import Base


class PrimaryKeyIdMixin:
    id = Column(Integer, primary_key=True, autoincrement=True)


class PDV(Base, PrimaryKeyIdMixin):
    __tablename__ = 'pdvs'

    trading_name = Column(String)
    owner_name = Column(String)
    document = Column(String, unique=True)
    coverage_area = Column(Geometry('MULTIPOLYGON'))
    address = Column(Geometry('POINT'))