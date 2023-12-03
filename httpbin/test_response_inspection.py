import requests


URL = 'https://httpbin.org/'


def test_cache_unmodified():
    response = requests.get(f'{URL}/cache')

    assert response.status_code == 200


def test_cache_modified():
    response = requests.get(f'{URL}/cache', headers={
        'If-Modified-Since': 'mod',
        'If-None-Match': 'mod',
    })

    assert response.status_code == 304


def test_cache_value():
    value = '1'
    response = requests.get(f'{URL}/cache/{value}')

    assert response.status_code == 200


def test_etag():
    response = requests.get(f'{URL}/etag/{{etag}}')

    assert response.status_code == 200


def test_etag_if_none_match():
    response = requests.get(f'{URL}/etag/{{etag}}', headers={
        'If-None-Match': 'test',
    })

    assert response.status_code == 200


def test_etag_if_match():
    response = requests.get(f'{URL}/etag/{{etag}}', headers={
        'If-Match': 'test',
    })

    assert response.status_code == 412


def test_get_response_headers_without_data():
    response = requests.get(f'{URL}/response-headers')

    assert response.status_code == 200
    assert response.json().get('Content-Length') == '68'


def test_get_response_headers_with_data():
    value = 'test_string'

    response = requests.get(f'{URL}/response-headers?freeform={value}')

    assert response.status_code == 200
    assert response.json().get('Content-Length') == '98'
    assert response.json().get('freeform') == value


def test_post_response_headers_without_data():
    response = requests.post(f'{URL}/response-headers')

    assert response.status_code == 200
    assert response.json().get('Content-Length') == '68'


def test_post_response_headers_with_data():
    value = 'test_string'

    response = requests.post(f'{URL}/response-headers?freeform={value}')

    assert response.status_code == 200
    assert response.json().get('Content-Length') == '98'
    assert response.json().get('freeform') == value
