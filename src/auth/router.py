from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from auth.schemas import UserCreate
from auth import service


router = APIRouter(
    prefix="/api/v0/auth",
    tags=["Auth"]
)


@router.get("/admin/all_users/")
async def get_all_users(session: AsyncSession = Depends(get_async_session)):
    return await service.view_all_users(session)


@router.post("/admin/add_user/")
async def register_user(new_user: UserCreate,
                        session: AsyncSession = Depends(get_async_session)):
    return await service.add_user(new_user, session)
