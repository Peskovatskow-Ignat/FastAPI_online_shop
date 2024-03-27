from typing import Any, Coroutine

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from webapp.models.shop.user import User


async def get_user_by_id(session: AsyncSession, user_id: int) -> Coroutine:
    return await session.get(User, user_id)


async def check_user(session: AsyncSession, email: str) -> Coroutine:
    print(await session.scalar(select(User).where(User.email == email)))
    return await session.scalar(select(User).where(User.email == email))
