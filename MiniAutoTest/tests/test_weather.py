import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from utils.request_util import get

def test_beijing():
    data = get("http://httpbin.org/get", params={"city": "Beijing"})
    assert data["args"]["city"] == "Beijing"

def test_shanghai():
    data = get("http://httpbin.org/get", params={"city": "Shanghai"})
    assert data["args"]["city"] == "Shanghai"

def test_guangzhou():
    data = get("http://httpbin.org/get", params={"city": "Guangzhou"})
    assert data["args"]["city"] == "Guangzhou"

def test_shenzhen():
    data = get("http://httpbin.org/get", params={"city": "Shenzhen"})
    assert data["args"]["city"] == "Shenzhen"

def test_chengdu():
    data = get("http://httpbin.org/get", params={"city": "Chengdu"})
    assert data["args"]["city"] == "Chengdu"
