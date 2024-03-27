from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.responses import Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from webapp.api.v1.crud.user.router import user_router
from webapp.auth.jwt import get_user_id, oauth2_scheme
from webapp.crud.user.delete import delete_user_by_id
from webapp.integrations.postgres import get_session


@user_router.delete('', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    access_token: Annotated[OAuth2PasswordRequestForm, Depends(oauth2_scheme)],
    session: AsyncSession = Depends(get_session),
) -> Response:
    user_id = get_user_id(access_token)
    user = await delete_user_by_id(session, user_id)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
