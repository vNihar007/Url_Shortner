import time

def test_expired_url(client):
    res = client.post('/api/shorten', json={"url": "https://temp.com", "expires_in": 1})
    code = res.get_json()["short_code"]
    time.sleep(2)
    r = client.get(f'/{code}')
    assert r.status_code == 410
