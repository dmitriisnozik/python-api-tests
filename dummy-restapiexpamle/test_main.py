import requests
from fake_useragent import UserAgent
from faker import Faker


URL = 'https://dummy.restapiexample.com/api/v1'
ua = UserAgent()
fake = Faker()


def test_get_employees_data():
    response = requests.get(
        f'{URL}/employees',
        headers={
            'User-Agent': ua.random,
        }
    )

    assert response.status_code == 200
    assert response.json().get('status') == 'success'


def test_get_single_employee():
    response = requests.get(
        f'{URL}/employee/1',
        headers={
            'User-Agent': ua.random,
        }
    )

    data = response.json().get('data')

    assert response.status_code == 200
    assert response.json().get('status') == 'success'
    assert data['id'] == 1
    assert data['employee_name'] == 'Tiger Nixon'


def test_create_new_employee():
    data = {
        'name': fake.first_name(),
        'salary': '120000',
        'age': '35',
    }

    response = requests.post(
        f'{URL}/create',
        data=data,
        headers={
            'User-Agent': ua.random,
        }
    )

    assert response.status_code == 200
    assert response.json().get('status') == 'success'
    assert list(response.json().get('data').items())[:3] == list(data.items())


def test_update_employee():
    data = {
        'name': fake.first_name(),
        'salary': '120000',
        'age': '35',
    }

    response = requests.put(
        f'{URL}/update/21',
        data=data,
        headers={
            'User-Agent': ua.random,
        }
    )

    assert response.status_code == 200
    assert response.json().get('status') == 'success'
    assert list(response.json().get('data').items())[:3] == list(data.items())


def test_delete_employee():
    response = requests.delete(
        f'{URL}/delete/2',
        headers={
            'User-Agent': ua.random,
        }
    )

    assert response.status_code == 200
    assert response.json().get('status') == 'success'
    assert response.json().get('data') == '2'
