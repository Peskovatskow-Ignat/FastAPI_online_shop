from sqlalchemy.ext.asyncio import AsyncSession

from webapp.auth.password import hash_password
from webapp.models.shop.user import User
from webapp.schema.shop.user import UserData


async def update_user_by_id(session: AsyncSession, user_id: int, user_info: UserData) -> User:

    user_to_update = await session.get(User, user_id)

    user_info_dict = user_info.model_dump()
    for attr, val in user_info_dict.items():
        if attr == 'password':
            setattr(user_to_update, attr, hash_password(val))
        else:
            setattr(user_to_update, attr, val)

    await session.commit()
    return user_to_update
