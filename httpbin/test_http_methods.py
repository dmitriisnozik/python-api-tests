import requests


URL = 'https://httpbin.org/'


def test_get_method():
    response = requests.get(f'{URL}/get')

    assert response.status_code == 200


def test_post_method():
    response = requests.post(f'{URL}/post')

    assert response.status_code == 200


def test_put_method():
    response = requests.put(f'{URL}/put')

    assert response.status_code == 200


def test_patch_method():
    response = requests.patch(f'{URL}/patch')

    assert response.status_code == 200


def test_delete_method():
    response = requests.delete(f'{URL}/delete')

    assert response.status_code == 200
