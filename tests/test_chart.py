def test_chart_png(client):
    res = client.post('/api/shorten', json={"url": "https://openai.com"})
    code = res.get_json()["short_code"]

    # Trigger click
    client.get(f'/{code}')
    chart = client.get(f'/api/stats/{code}/chart')

    assert chart.status_code == 200
    assert chart.headers['Content-Type'] == 'image/png'
