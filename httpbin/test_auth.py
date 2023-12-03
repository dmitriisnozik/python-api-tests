import requests
from requests.auth import HTTPDigestAuth, HTTPBasicAuth


URL = 'https://httpbin.org/'


def test_basic_auth_positive():
    username = 'user'
    password = 'passwd'

    auth = HTTPBasicAuth(username, password)

    response = requests.get(f'{URL}/basic-auth/{username}/{password}', auth=auth)

    assert response.status_code == 200
    assert response.json().get('authenticated') is True
    assert response.json().get('user') == username


def test_basic_auth_negative():
    username = 'user'
    password = 'passwd'

    auth = HTTPBasicAuth(username, password)

    response = requests.get(f'{URL}/basic-auth/{username}/{password}123', auth=auth)

    assert response.status_code == 401


def test_bearer_auth_positive():
    token = 'token'

    response = requests.get(f'{URL}/bearer', headers={
        'Authorization': f'Bearer {token}'
    })

    assert response.status_code == 200
    assert response.json().get('authenticated') is True
    assert response.json().get('token') == token


def test_bearer_auth_negative():
    response = requests.get(f'{URL}/bearer')

    assert response.status_code == 401


def test_digest_auth_positive():
    username = 'user'
    password = 'passwd'
    auth = HTTPDigestAuth(username, password)

    response = requests.get(f'{URL}digest-auth/qop/{username}/{password}', auth=auth, stream=True)

    assert response.status_code == 200
    assert response.json().get('authenticated') is True
    assert response.json().get('user') == username


def test_digest_auth_negative():
    username = 'user'
    password = 'passwd'
    auth = HTTPDigestAuth(username, password)

    response = requests.get(f'{URL}digest-auth/qop/{username}/{password}123', auth=auth, stream=True)

    assert response.status_code == 401


def test_digest_with_algorithm_md5_positive():
    username = 'user'
    password = 'passwd'
    auth = HTTPDigestAuth(username, password)

    response = requests.get(f'{URL}digest-auth/qop/{username}/{password}/MD5', auth=auth, stream=True)

    assert response.status_code == 200
    assert response.json().get('authenticated') is True
    assert response.json().get('user') == username


def test_digest_with_algorithm_sha256_positive():
    username = 'user'
    password = 'passwd'
    auth = HTTPDigestAuth(username, password)

    response = requests.get(f'{URL}digest-auth/qop/{username}/{password}/SHA-256', auth=auth, stream=True)

    assert response.status_code == 200
    assert response.json().get('authenticated') is True
    assert response.json().get('user') == username


def test_digest_with_algorithm_sha512_positive():
    username = 'user'
    password = 'passwd'
    auth = HTTPDigestAuth(username, password)

    response = requests.get(f'{URL}digest-auth/qop/{username}/{password}/SHA-512', auth=auth, stream=True)

    assert response.status_code == 200
    assert response.json().get('authenticated') is True
    assert response.json().get('user') == username


def test_digest_stale_after():
    username = 'user'
    password = 'passwd'
    auth = HTTPDigestAuth(username, password)

    response = requests.get(f'{URL}digest-auth/qop/{username}/{password}/MD5/never', auth=auth, stream=True)

    assert response.status_code == 200
    assert response.json().get('authenticated') is True
    assert response.json().get('user') == username


def test_hidden_basic_auth_positive():
    username = 'user'
    password = 'passwd'

    auth = HTTPBasicAuth(username, password)

    response = requests.get(f'{URL}/hidden-basic-auth/{username}/{password}', auth=auth)

    assert response.status_code == 200
    assert response.json().get('authenticated') is True
    assert response.json().get('user') == username


def test_hidden_basic_auth_negative():
    username = 'user'
    password = 'passwd'

    auth = HTTPBasicAuth(username, password)

    response = requests.get(f'{URL}/hidden-basic-auth/{username}/{password}123', auth=auth)

    assert response.status_code == 404
