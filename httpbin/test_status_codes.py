import requests


URL = 'https://httpbin.org/'


def test_delete_status_codes():
    response200 = requests.delete(f'{URL}/status/200')
    response300 = requests.delete(f'{URL}/status/300')
    response400 = requests.delete(f'{URL}/status/400')
    response500 = requests.delete(f'{URL}/status/500')

    assert response200.status_code == 200
    assert response300.status_code == 300
    assert response400.status_code == 400
    assert response500.status_code == 500


def test_get_status_codes():
    response200 = requests.get(f'{URL}/status/200')
    response300 = requests.get(f'{URL}/status/300')
    response400 = requests.get(f'{URL}/status/400')
    response500 = requests.get(f'{URL}/status/500')

    assert response200.status_code == 200
    assert response300.status_code == 300
    assert response400.status_code == 400
    assert response500.status_code == 500


def test_patch_status_codes():
    response200 = requests.patch(f'{URL}/status/200')
    response300 = requests.patch(f'{URL}/status/300')
    response400 = requests.patch(f'{URL}/status/400')
    response500 = requests.patch(f'{URL}/status/500')

    assert response200.status_code == 200
    assert response300.status_code == 300
    assert response400.status_code == 400
    assert response500.status_code == 500


def test_post_status_codes():
    response200 = requests.post(f'{URL}/status/200')
    response300 = requests.post(f'{URL}/status/300')
    response400 = requests.post(f'{URL}/status/400')
    response500 = requests.post(f'{URL}/status/500')

    assert response200.status_code == 200
    assert response300.status_code == 300
    assert response400.status_code == 400
    assert response500.status_code == 500


def test_put_status_codes():
    response200 = requests.put(f'{URL}/status/200')
    response300 = requests.put(f'{URL}/status/300')
    response400 = requests.put(f'{URL}/status/400')
    response500 = requests.put(f'{URL}/status/500')

    assert response200.status_code == 200
    assert response300.status_code == 300
    assert response400.status_code == 400
    assert response500.status_code == 500
