from flask import jsonify

def test_redirect_valid(client):
    res = client.post('/api/shorten', json={"url": "https://google.com"})
    code = res.get_json()["short_code"]

    r = client.get(f'/{code}', follow_redirects=False)
    assert r.status_code == 302
    assert r.headers['Location'] == "https://google.com"

def test_redirect_invalid(client):
    r = client.get('/doesnotexist')
    assert r.status_code == 404


