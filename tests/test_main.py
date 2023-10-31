from httpx import AsyncClient


async def test_root(ac: AsyncClient) -> None:
    response = await ac.get("/")
    assert response.status_code == 200
    assert response.json()['status'] == 'running'
    assert response.json()['api_version'] == '0.1'
    assert response.json()['message'] == 'Welcome to the IVLEV_AUTH!'
