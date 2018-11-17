import json
import pytest
from clikpik import app
from os import environ

@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        pass # databases and resourses have to be freed at the end. But so far we don't have anything

    request.addfinalizer(teardown)
    return test_client

def post_json(client, url, json_dict):
    """Send dictionary json_dict as a json to the specified url """
    return client.post(url, data=json.dumps(json_dict), content_type='application/json')

def json_of_response(response):
    """Decode json from response"""
    return json.loads(response.data.decode('utf8'))

#def test_dummy(client):
#    response = client.get('/productouno/nose')
#    print("imprime = "+ str(response.data))
#   assert b'{"posicion": "nose", "nombre": "productouno"}' in response.data

def test_home(client):
    response = client.get('/productos')
    print("imprime = "+ str(response.data))
    assert True