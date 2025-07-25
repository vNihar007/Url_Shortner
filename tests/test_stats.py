def test_stats_response(client):
    res = client.post('/api/shorten', json={"url": "https://github.com"})
    code = res.get_json()["short_code"]

    # Trigger click
    client.get(f'/{code}')

    stat = client.get(f'/api/stats/{code}')
    assert stat.status_code == 200
    data = stat.get_json()
    assert "clicks" in data
    assert data["clicks"] >= 1
