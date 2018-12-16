import requests
from src.delivery.models import PDV
from src.delivery.utils import geo_utils

from sqlalchemy import text
from src.infra.database import engine

response = requests.get('https://raw.githubusercontent.com/ZeLabs/code-challenge/master/files/pdvs.json')

data = response.json()
pdvs = data['pdvs']


for pdv in pdvs:
    to_store = PDV(trading_name=pdv['tradingName'],
        owner_name=pdv['ownerName'],
        document=pdv['document'],
        coverage_area=geo_utils.to_wkt(pdv['coverageArea']),
        address=geo_utils.to_wkt(pdv['address']))
    query = text('insert into pdvs(trading_name, owner_name, document, coverage_area, address) '
                 f'values(\'{to_store.trading_name}\', \'{to_store.owner_name}\','
                 f'\'{to_store.document}\', \'{to_store.coverage_area}\', \'{to_store.address}\')')

    engine.execute(query)

