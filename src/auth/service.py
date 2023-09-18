import uuid

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from auth.models import User, Profile
from auth.schemas import UserCreate


async def view_all_users(session: AsyncSession):
    """View all users(limit=10)"""
    query = (
            select(User, Profile)
            .join(Profile, User.id == Profile.user_id)
            .limit(10)
            )
    result = await session.execute(query)
    return [dict(r._mapping) for r in result.all()]


async def add_user(user: UserCreate, session):
    """Add user and additional add profile(info by user)."""
    context = user.model_dump()
    context['id'] = uuid.uuid4()
    stmt = insert(User).values(**context)
    await session.execute(stmt)

    query = select(User.id).filter(User.email == context['email'])
    user_id = await session.execute(query)
    stmt = insert(Profile).values(
        id=uuid.uuid4(),
        user_id=user_id.scalar()
        )
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
