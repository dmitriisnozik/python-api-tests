import requests


URL = 'https://httpbin.org/'


def test_brotli():
    response = requests.get(f'{URL}/brotli')

    assert response.status_code == 200
    assert response.json().get('brotli') is True


def test_deflate():
    response = requests.get(f'{URL}/deflate')

    assert response.status_code == 200
    assert response.json().get('deflated') is True


def test_deny():
    response = requests.get(f'{URL}/deny')

    assert response.status_code == 200


def test_utf8():
    response = requests.get(f'{URL}/encoding/utf8')

    assert response.status_code == 200
    assert response.encoding == 'utf-8'


def test_html():
    response = requests.get(f'{URL}/html')

    assert response.status_code == 200
    assert '<!DOCTYPE html>' in str(response.content)


def test_json():
    response = requests.get(f'{URL}/json')

    assert response.status_code == 200
    assert response.json()


def test_robots_txt():
    response = requests.get(f'{URL}/robots.txt')

    assert response.status_code == 200
    assert response.content == b'User-agent: *\nDisallow: /deny\n'


def test_xml():
    response = requests.get(f'{URL}/xml')

    assert response.status_code == 200
