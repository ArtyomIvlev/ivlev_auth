from httpx import AsyncClient


data_user = {
    "email": "user@example.com",
    "password": "string"
}


async def test_add_user_with_correct_data(ac: AsyncClient) -> None:
    response = await ac.post("/api/v0/auth/admin/add_user/", json=data_user)
    assert response.status_code == 200
    response = await ac.post("/api/v0/auth/admin/add_user/", json=data_user)
    assert response.status_code == 400
    response = await ac.post("/api/v0/auth/admin/add_user/", json={
        "email": "user.com",
        "password": "string"
    })
    assert response.status_code == 422


async def test_get_all_users(ac: AsyncClient) -> None:
    response = await ac.get("/api/v0/auth/admin/all_users/")
    assert response.status_code == 200
    assert response.json()[0]["User"]["email"] == data_user["email"]
    assert response.json()[0]["Profile"]["user_id"] == response.json()[0]["User"]["id"]
    assert len(response.json()) == 1
