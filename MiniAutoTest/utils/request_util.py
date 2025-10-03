 
import requests

def get(url, params=None):
    """统一 GET 请求，返回 JSON"""
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    return r.json()
