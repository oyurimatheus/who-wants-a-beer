from contextlib import contextmanager

import graphene
from sqlalchemy.exc import SQLAlchemyError

from src.delivery.models import PDV
from src.delivery.objects import PDVObject
from src.infra.database import db_session
from src.delivery.utils import geo_utils


@contextmanager
def make_session_scope(Session=db_session):
    session = Session()
    session.expire_on_commit = False

    try:
        yield session
    except SQLAlchemyError:
        session.rollback()
        raise
    finally:
        session.close()


class CreatePDV(graphene.Mutation):

    class Input:
        trading_name = graphene.String()
        owner_name = graphene.String()
        document = graphene.String()
        coverage_area = graphene.String()
        address = graphene.String()

    pdv = graphene.Field(lambda: PDVObject)
    ok = graphene.Boolean()

    @staticmethod
    def mutate(request, info, **args):

        trading_name = args.get('trading_name', '')
        owner_name = args.get('owner_name', '')
        document = args.get('document', '')
        coverage_area = args.get('coverage_area', '{}')
        address = args.get('address', '{}')

        coverage_area = geo_utils.to_wkt(coverage_area)
        address = geo_utils.to_wkt(address)

        with make_session_scope() as session:
            pdv = PDV(trading_name=trading_name,
                      owner_name=owner_name,
                      document=document,
                      coverage_area=coverage_area,
                      address=address)

            session.add(pdv)
            session.commit()

        return CreatePDV(pdv=pdv, ok=True)
