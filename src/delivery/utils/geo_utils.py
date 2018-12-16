from src.delivery.objects import PDVObject
from geoalchemy2 import shape
import geojson
from shapely import geometry


def to_wkt(geo: 'str or geojson geometry type'):
    if isinstance(geo, str):
        geo = geojson.loads(geo)

    wkt = geometry.shape(geo)

    return wkt.wkt


def convert_wkt_pdv_to_geojson_pdv(pdv: PDVObject):
    pdv.coverage_area = geometry.mapping(shape.to_shape(pdv.coverage_area))
    pdv.address = geometry.mapping(shape.to_shape(pdv.address))

    return pdv
