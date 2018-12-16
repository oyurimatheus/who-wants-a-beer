import geoalchemy2.types
import graphene
from shapely import geometry
from sqlalchemy import text

from src.delivery.models import PDV
from src.delivery.mutations import CreatePDV
from src.delivery.objects import PDVObject
from src.delivery.utils import geo_utils
from src.infra.database import engine


class Query(graphene.ObjectType):
    pdv_by_id = graphene.Field(PDVObject, id=graphene.Int(), required=True,
                               description='Search a specific PDV from an ID number')
    nearest_pdv = graphene.Field(graphene.List(PDVObject), lng=graphene.Float(), lat=graphene.Float(), required=True,
                                 description='Search the ten nearest PDV from a longitude(lng) and latitude(lat) ')

    @staticmethod
    def resolve_pdv_by_id(request, context, **args):
        query = PDVObject.get_query(context)
        filtered_query = query.filter_by(**args)

        pdv = filtered_query.first()

        return geo_utils.convert_wkt_pdv_to_geojson_pdv(pdv)

    @staticmethod
    def resolve_nearest_pdv(request, context, **args):
        point = geometry.Point(args['lng'], args['lat'])

        query = text('select id, trading_name, owner_name, document, coverage_area, address from pdvs '
                     f'where ST_Covers(pdvs.coverage_area, \'{point}\') = true '
                     f'order by ST_Distance(pdvs.address, \'{point}\')')

        result = engine.execute(query)

        pdvs = []

        for raw in list(result):
            pdv = PDV(id=raw[0],
                     trading_name=raw[1],
                     owner_name=raw[2],
                     document=raw[3],
                     coverage_area=geoalchemy2.types.WKBElement(raw[4]),
                     address=geoalchemy2.types.WKBElement(raw[5]))

            pdv = geo_utils.convert_wkt_pdv_to_geojson_pdv(pdv)

            pdvs.append(pdv)

        return pdvs


class Mutations(graphene.ObjectType):
    create_pdv = CreatePDV.Field(description='Creates a new PDV. '
                                             'Given a trading name, owner name, document, coverage area and address')


schema = graphene.Schema(query=Query, mutation=Mutations)
