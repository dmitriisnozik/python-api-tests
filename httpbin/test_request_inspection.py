import requests
from fake_useragent import FakeUserAgent


URL = 'https://httpbin.org/'
ua = FakeUserAgent()


def test_headers():
    user_agent = ua.random

    response = requests.get(f'{URL}/headers', headers={
        'User-Agent': user_agent,
        'Accept': 'application/json',
    })

    headers = response.json().get('headers')

    assert response.status_code == 200
    assert headers['User-Agent'] == user_agent
    assert headers['Accept'] == 'application/json'


def test_ip():
    response = requests.get(f'{URL}/ip')
    response2 = requests.get('http://ip-api.com/json/')

    assert response.status_code == 200
    assert response.json().get('origin') == response2.json().get('query')



def test_user_agent():
    user_agent = ua.random

    response = requests.get(f'{URL}/user-agent', headers={
        'User-Agent': user_agent,
    })

    assert response.status_code == 200
    assert response.json().get('user-agent') == user_agent
