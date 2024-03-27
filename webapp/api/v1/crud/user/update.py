from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from webapp.api.v1.crud.user.router import user_router
from webapp.auth.jwt import get_user_id, oauth2_scheme
from webapp.crud.user.update import update_user_by_id
from webapp.integrations.postgres import get_session
from webapp.schema.shop.user import UserData, UserResp


@user_router.put('', status_code=status.HTTP_200_OK, response_model=UserResp)
async def update_user(
    user_info: UserData,
    access_token: Annotated[OAuth2PasswordRequestForm, Depends(oauth2_scheme)],
    session: AsyncSession = Depends(get_session),
) -> UserResp:
    user_id = get_user_id(access_token)
    try:
        user = await update_user_by_id(session, user_id, user_info)
    except Exception as ex:
        print(ex)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    return user
