import pytest
from typing import Dict
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import User


@pytest.mark.parametrize(
    'user, status',
    [
        ({"email": "user@example.com", "password": "string"}, 200),
        ({"email": "user@example.com", "password": "string"}, 400),
        ({"email": "user", "password": "string"}, 422),
    ]
)
async def test_add_user(user: Dict[str, str],
                        user_data: Dict[str, str],
                        ac: AsyncClient, status: int,
                        db_session: AsyncSession) -> None:
    response = await ac.post("/api/v0/auth/admin/add_user/", json=user)
    assert response.status_code == status
    if response.status_code == 200:
        query = select(User).where(User.email == user_data['email'])
        user = await db_session.scalar(query)
        assert user is not None


async def test_get_all_users(user_data: Dict[str, str], ac: AsyncClient) -> None:
    response = await ac.get("/api/v0/auth/admin/all_users/")
    assert response.status_code == 200
    assert response.json()[0]["User"]["email"] == user_data["email"]
    assert response.json()[0]["Profile"]["user_id"] == response.json()[0]["User"]["id"]
    assert len(response.json()) == 1
