import requests
import random


URL = 'https://httpbin.org/'


def test_base64_positive():
    value = 'SFRUUEJJTiBpcyBhd2Vzb21l'

    response = requests.get(f'{URL}/base64/{value}')

    assert response.status_code == 200
    assert response.content == b'HTTPBIN is awesome'


def test_base64_negative():
    value = 'nonbase64'

    response = requests.get(f'{URL}/base64/{value}')

    assert response.status_code == 200
    assert response.content == b'Incorrect Base64 data try: SFRUUEJJTiBpcyBhd2Vzb21l'


def test_bytes_positive():
    n = '1'

    response = requests.get(f'{URL}/bytes/{n}')

    assert response.status_code == 200


def test_bytes_negative():
    n = 'test'

    response = requests.get(f'{URL}/bytes/{n}')

    assert response.status_code == 404


def test_delete_delay():
    response = requests.delete(f'{URL}/delay/1')

    assert response.status_code == 200


def test_get_delay():
    response = requests.get(f'{URL}/delay/1')

    assert response.status_code == 200


def test_patch_delay():
    response = requests.patch(f'{URL}/delay/1')

    assert response.status_code == 200


def test_post_delay():
    response = requests.post(f'{URL}/delay/1')

    assert response.status_code == 200


def test_put_delay():
    response = requests.put(f'{URL}/delay/1')

    assert response.status_code == 200


def test_drip():
    code = random.randint(100, 599)

    response = requests.get(f'{URL}/drip?code={code}')

    assert response.status_code == code


def test_links():
    n = random.randint(1, 10)
    offset = 11

    response = requests.get(f'{URL}/links/{n}/{offset}')

    assert str(response.content).count('<a href=') == n


def test_range():
    numbytes = 12

    response = requests.get(f'{URL}/range/{numbytes}')

    assert response.status_code == 200


def test_stream_bytes_range():
    n = 1

    response = requests.get(f'{URL}/stream-bytes/{n}')

    assert response.status_code == 200


def test_stream_json():
    n = 1

    response = requests.get(f'{URL}/stream/{n}')

    assert response.status_code == 200
    assert response.json()


def test_uuid():
    response = requests.get(f'{URL}/uuid')

    assert response.status_code == 200
    assert response.json().get('uuid')
