from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import parse_obj_as
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from webapp.api.v1.crud.user.router import user_router
from webapp.auth.jwt import get_user_id, oauth2_scheme
from webapp.crud.user.read import get_user_by_id
from webapp.integrations.postgres import get_session
from webapp.schema.shop.user import UserResp


@user_router.get('', status_code=status.HTTP_200_OK, response_model=UserResp)
async def get_user(
    access_token: Annotated[OAuth2PasswordRequestForm, Depends(oauth2_scheme)],
    session: AsyncSession = Depends(get_session),
):
    user_id = get_user_id(access_token)
    user = await get_user_by_id(session, user_id)

    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    return parse_obj_as(UserResp, user)
