import graphene

from src.delivery.mutations import CreatePDV
from src.delivery.objects import PDVObject


class Query(graphene.ObjectType):

    pdv = graphene.Field(PDVObject, id=graphene.Int())

    def resolve_pdv(self, args, context):
        query = PDVObject.get_query(context)
        filtered_query = query.filter_by(**args)

        return filtered_query.first()


class Mutations(graphene.ObjectType):
    create_pdv= CreatePDV.Field(description='Creates a new PDV. '
                                        'Given a trading name, owner name, document, coverage area and address')

schema = graphene.Schema(query=Query, mutation=Mutations)
