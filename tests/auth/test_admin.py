from httpx import AsyncClient


async def test_add_user(ac: AsyncClient) -> None:
    response = await ac.post("/api/v0/auth/admin/add_user/", json={
        "email": "user@example.com",
        "password": "string"
    })
    assert response.status_code == 200


async def test_add_user_repeat(ac: AsyncClient) -> None:
    response = await ac.post("/api/v0/auth/admin/add_user/", json={
        "email": "user@example.com",
        "password": "string"
    })
    assert response.status_code == 400


async def test_add_user_wrong_email(ac: AsyncClient) -> None:
    response = await ac.post("/api/v0/auth/admin/add_user/", json={
        "email": "user.com",
        "password": "string"
    })
    assert response.status_code == 422


async def test_get_all_users(ac: AsyncClient) -> None:
    response = await ac.get("/api/v0/auth/admin/all_users/")
    assert response.status_code == 200
    assert response.json()[0]['User']['email'] == 'user@example.com'
    assert response.json()[0]['Profile']['user_id'] == response.json()[0]['User']['id']
    assert len(response.json()) == 1
