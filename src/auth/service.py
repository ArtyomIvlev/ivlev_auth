import uuid

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from auth.models import User, Profile
from auth.schemas import UserCreate


async def view_all_users(session: AsyncSession):
    """View all users(limit=10)"""
    try:
        query = (
                select(User, Profile)
                .join(Profile, User.id == Profile.user_id)
                .limit(10)
                )
        result = await session.execute(query)
        return [dict(r._mapping) for r in result.all()]
    finally:
        await session.close()


async def add_user(user: UserCreate, session):
    """Add user and additionl add profile(info by user)."""
    try:
        context = user.model_dump()
        context['id'] = uuid.uuid4()
        stmt = insert(User).values(**context)
        await session.execute(stmt)

        q = select(User.id).filter(User.email == context['email'])
        user_id = await session.execute(q)
        stmt = insert(Profile).values(
            id=uuid.uuid4(),
            user_id=user_id.scalar()
            )
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}
    finally:
        await session.close()
