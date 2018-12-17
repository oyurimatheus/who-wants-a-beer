import requests

from tests.constants import API_URL


def test_should_return_the_nearest_pdv_when_given_a_lat_lng():
    query = {'query': '{nearestPdv(lng: -46.44016, lat: -23.61494){ownerName, tradingName}}'}
    response = requests.post(API_URL, json=query)
    data = response.json()
    nearest_pdv = data['data']['nearestPdv'][0]

    assert nearest_pdv['ownerName'] == 'Pedro Silva'


def test_should_return_the_pdv_when_given_the_id():
    query = {'query': '{pdvById(id: 3){ownerName, tradingName}}'}
    response = requests.post(API_URL, json=query)
    data = response.json()
    pdv = data['data']['pdvById']

    assert len(pdv.keys()) == 2
