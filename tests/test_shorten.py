import pytest
import json

def test_shorten_valid(client):
    res = client.post('/api/shorten', json={"url": "https://example.com"})
    assert res.status_code == 200
    data = res.get_json()
    assert "short_code" in data
    assert "short_url" in data

def test_shorten_invalid_url(client):
    res = client.post('/api/shorten', json={"url": "not-a-url"})
    assert res.status_code == 400
