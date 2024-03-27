from typing import Annotated, Any

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from webapp.api.v1.crud.user.router import user_router
from webapp.auth.jwt import oauth2_scheme
from webapp.crud.user.create import create_user
from webapp.integrations.postgres import get_session
from webapp.schema.shop.user import UserData, UserResp


@user_router.post('', status_code=status.HTTP_201_CREATED, response_model=UserResp)
async def create(
    body: UserData,
    access_token: Annotated[OAuth2PasswordRequestForm, Depends(oauth2_scheme)],
    session: AsyncSession = Depends(get_session),
) -> dict[str, Any]:
    try:
        user = await create_user(session, body)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    return user
