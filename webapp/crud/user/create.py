from sqlalchemy.ext.asyncio import AsyncSession

from webapp.crud.user.read import check_user
from webapp.models.shop.user import User
from webapp.schema.shop.user import UserData


async def create_user(session: AsyncSession, user_data: UserData) -> User | bool:

    if await check_user(session, user_data.dict().get('email', None)):
        return False

    user = User(**user_data.dict())

    async with session.begin_nested():
        session.add(user)
        await session.flush()
        await session.commit()

    return user
