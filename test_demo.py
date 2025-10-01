import requests

def test_demo():
    r = requests.get('http://httpbin.org/get')
    assert r.status_code == 200