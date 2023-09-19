from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.auth.schemas import UserCreate
from src.auth import service


router = APIRouter(
    prefix="/api/v0/auth",
    tags=["Auth"]
)


@router.get("/admin/all_users/")
async def get_all_users(session: AsyncSession = Depends(get_async_session)):
    try:
        result = await service.view_all_users(session)
        return result
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.post("/admin/add_user/")
async def add_user(new_user: UserCreate,
                   session: AsyncSession = Depends(get_async_session)):
    result = await service.add_user(new_user, session)
    return result
