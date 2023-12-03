import requests


URL = 'https://reqres.in'


def test_list_users():
    response = requests.get(f'{URL}/api/users?page=2')

    assert response.status_code == 200
    assert response.json().get('page') == 2


def test_users_have_id_in_avatar():
    response = requests.get(f'{URL}/api/users?page=2')

    data = response.json().get('data')

    for item in data:
        assert str(item['id']) in item['avatar']


def test_user_email_at_reqres_domain():
    response = requests.get(f'{URL}/api/users?page=2')

    data = response.json().get('data')

    for item in data:
        assert item['email'].endswith('@reqres.in')


def test_get_resources_list():
    response = requests.get(f'{URL}/api/unknown')

    assert response.status_code == 200
    assert response.json().get('page') == 1


def test_resources_order_test():
    response = requests.get(f'{URL}/api/unknown')

    data = response.json().get('data')
    year_order = [x['year'] for x in data]

    assert year_order == sorted(year_order)


def test_single_user():
    expected = {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    }

    response = requests.get(f'{URL}/api/users/2')

    assert response.status_code == 200
    assert response.json().get('data') == expected


def test_single_user_not_found():
    response = requests.get(f'{URL}/api/users/23')

    assert response.status_code == 404


def test_single_resource():
    expected = {
        "id": 2,
        "name": "fuchsia rose",
        "year": 2001,
        "color": "#C74375",
        "pantone_value": "17-2031"
    }

    response = requests.get(f'{URL}/api/unknown/2')

    assert response.status_code == 200
    assert response.json().get('data') == expected


def test_single_resource_not_found():
    response = requests.get(f'{URL}/api/unknown/23')

    assert response.status_code == 404


def test_register_positive():
    expected = {
        "id": 4,
        "token": "QpwL5tke4Pnpja7X4"
    }
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    response = requests.post(f'{URL}/api/register', data=data)

    assert response.status_code == 200
    assert response.json() == expected


def test_register_negative():
    data = {
        "email": "sydney@fife",
    }

    response = requests.post(f'{URL}/api/register', data=data)

    assert response.status_code == 400
    assert response.json().get('error') == 'Missing password'


def test_login_positive():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    expected = {
        "token": "QpwL5tke4Pnpja7X4"
    }

    response = requests.post(f'{URL}/api/login', data=data)

    assert response.status_code == 200
    assert response.json() == expected


def test_login_negative():
    data = {
        "email": "peter@klaven",
    }

    response = requests.post(f'{URL}/api/login', data=data)

    assert response.status_code == 400
    assert response.json().get('error') == 'Missing password'


def test_create_method():
    data = {
        "name": "morpheus",
        "job": "leader"
    }

    response = requests.post(f'{URL}/api/users', data=data)

    assert response.status_code == 201
    assert response.json().get('name') == data['name']
    assert response.json().get('job') == data['job']


def test_put_method():
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = requests.put(f'{URL}/api/users', data=data)

    assert response.status_code == 200
    assert response.json().get('name') == data['name']
    assert response.json().get('job') == data['job']


def test_patch_method():
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = requests.patch(f'{URL}/api/users', data=data)

    assert response.status_code == 200
    assert response.json().get('name') == data['name']
    assert response.json().get('job') == data['job']


def test_delete_method():
    response = requests.patch(f'{URL}/api/users/2')

    assert response.status_code == 204
