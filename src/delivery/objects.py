import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from src.delivery.models import PDV


class PDVObject(SQLAlchemyObjectType):

    id = graphene.Int()

    class Meta:
        model = PDV
