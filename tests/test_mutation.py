from random import randrange

import requests

from tests.constants import API_URL


def test_should_create_a_pdv_when_given_the_correct_props():
    variables = {'ownerName': '"Chico"',
                 'tradingName': '"Buteco do Chico"',
                 'document': f'"{randrange(1000, 99999)}"',
                 'address': '"{ \\"type\\": \\"Point\\",\\"coordinates\\": [-46.57421, -21.785741]}"',
                 'coverageArea': '"{\\"type\\": \\"MultiPolygon\\", \\"coordinates\\": [[[[30.0, 20.0], [45.0, 40.0],'
                                 '[10.0, 40.0],  [30.0, 20.0]]], '
                                 '[[[15.0, 5.0], [40.0, 10.0], [10.0, 20.0], [5.0, 10.0], [15.0, 5.0]]]]}"'
                 }

    mutation = '''mutation {{ createPdv(ownerName: {ownerName},
        tradingName: {tradingName},
        document: {document},
        address: {address},
        coverageArea: {coverageArea}) {{
            ok
        }}
    }}'''.format(**variables)

    response = requests.post(API_URL, json={'query': mutation})

    data = response.json()

    created = data['data']['createPdv']

    assert created['ok']



