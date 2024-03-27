from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from webapp.api.v1.crud.product.router import product_router
from webapp.auth.jwt import get_user_id, oauth2_scheme
from webapp.crud.product.delete import delete_product_by_id
from webapp.integrations.postgres import get_session


@product_router.delete('/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product_id: int,
    access_token: Annotated[OAuth2PasswordRequestForm, Depends(oauth2_scheme)],
    session: AsyncSession = Depends(get_session),
) -> None:

    user_id = get_user_id(access_token)

    cart = await delete_product_by_id(session, product_id, user_id)

    if not cart:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
