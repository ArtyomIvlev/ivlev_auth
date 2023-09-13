from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from auth.models import User
from auth.schemas import UserCreate


router = APIRouter(
    prefix="/api/v0/auth",
    tags=["Auth"]
)


@router.get("/")
async def get_all_users(session: AsyncSession = Depends(get_async_session)):
    query = select(User)
    result = await session.execute(query)
    return [dict(r._mapping) for r in result.all()]


@router.post("/")
async def add_user(new_user: UserCreate,
                   session: AsyncSession = Depends(get_async_session)):
    stmt = insert(User).values(**new_user.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
