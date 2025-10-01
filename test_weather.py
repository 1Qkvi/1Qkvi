import requests

def test_beijing():
    r = requests.get('http://httpbin.org/get', params={"city": "Beijing"})
    assert r.status_code == 200

def test_shanghai():
    r = requests.get('http://httpbin.org/get', params={"city": "Shanghai"})
    assert r.status_code == 200

def test_guangzhou():
    r = requests.get('http://httpbin.org/get', params={"city": "Guangzhou"})
    assert r.status_code == 200

def test_shenzhen():
    r = requests.get('http://httpbin.org/get', params={"city": "Shenzhen"})
    assert r.status_code == 200

def test_chengdu():
    r = requests.get('http://httpbin.org/get', params={"city": "Chengdu"})
    assert r.status_code == 200
