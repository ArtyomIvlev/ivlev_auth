import uuid

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from auth.models import User, Profile
from auth.exceptions import EmailExists
from auth.schemas import UserCreate


async def get_user_by_email(email: str, session: AsyncSession):
    # """Return user by email."""
    query = select(User).where(User.email == email)
    user = await session.scalar(query)
    return user


async def view_all_users(session: AsyncSession):
    """View all users(limit=10)"""
    query = (select(User, Profile)
             .join(Profile, User.id == Profile.user_id)
             .limit(10)
             )
    result = await session.execute(query)
    return [dict(r._mapping) for r in result.all()]


async def add_user(user: UserCreate, session: AsyncSession):
    """Add user and additional add profile(info by user)."""
    context = user.model_dump()
    db_user = await get_user_by_email(email=context['email'], session=session)
    if db_user:
        raise EmailExists()
    context['id'] = uuid.uuid4()
    stmt = insert(User).values(**context)
    await session.execute(stmt)

    query = select(User.id).filter(User.email == context['email'])
    user_id = await session.execute(query)
    stmt = insert(Profile).values(id=uuid.uuid4(),
                                  user_id=user_id.scalar()
                                  )
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
