from contextlib import contextmanager

import graphene
from sqlalchemy.exc import SQLAlchemyError

from src.infra.database import db_session
from src.delivery.models import PDV
from src.delivery.objects import PDVObject

@contextmanager
def make_session_scope(Session=db_session):
    session = Session()
    session.expire_on_commit = False

    try:
        yield session
    except SQLAlchemyError:
        session.rowback()
        raise
    finally:
        session.close()

class CreatePDV(graphene.Mutation):

    class Input:
        trading_name = graphene.String()
        owner_name = graphene.String()
        document = graphene.String()
        # coverage_area = graphene.Scalar()
        # address = graphene.Scalar()

    pdv = graphene.Field(lambda: PDVObject)
    ok = graphene.Boolean()

    @staticmethod
    def mutate(request, info, **args):
        with make_session_scope as session:
            pdv = PDV(**args)

            session.add(pdv)
            session.commit()

            return CreatePDV(pdv=pdv, ok=True)
