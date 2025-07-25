def test_rate_limiting(client):
    for _ in range(10):
        res = client.post('/api/shorten', json={"url": "https://ratelimit.com"})
        assert res.status_code == 200

    res = client.post('/api/shorten', json={"url": "https://ratelimit.com"})
    assert res.status_code == 429
