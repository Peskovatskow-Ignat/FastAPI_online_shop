from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from webapp.auth.password import hash_password
from webapp.models.shop.user import User
from webapp.schema.shop.user import UserData


async def get_user(session: AsyncSession, user_info: UserData) -> User | None:
    return (
        await session.scalars(
            select(User).where(
                User.email == user_info.username,
                User.password == hash_password(user_info.password),
            )
        )
    ).one_or_none()
