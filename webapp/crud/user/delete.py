from sqlalchemy.ext.asyncio import AsyncSession

from webapp.models.shop.user import User


async def delete_user_by_id(session: AsyncSession, user_id: int) -> bool:

    user = await session.get(User, user_id)

    if user:
        await session.delete(user)
        await session.commit()
        return True

    return False
