from fastapi import Depends, HTTPException
from fastapi.responses import ORJSONResponse
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from webapp.api.v1.auth.router import auth_router
from webapp.auth.password import hash_password
from webapp.crud.user.create import create_user
from webapp.integrations.postgres import get_session
from webapp.schema.shop.user import UserData


@auth_router.post('/register')
async def register(
    body: UserData,
    session: AsyncSession = Depends(get_session),
) -> ORJSONResponse:
    body.password = hash_password(body.password)

    try:
        if not await create_user(session, body):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)

    return ORJSONResponse(content={'message': 'User created successfully'}, status_code=status.HTTP_201_CREATED)
