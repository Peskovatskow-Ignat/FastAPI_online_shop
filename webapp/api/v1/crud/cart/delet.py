from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.responses import Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from webapp.api.v1.crud.cart.router import cart_router
from webapp.auth.jwt import get_user_id, oauth2_scheme
from webapp.crud.cart.delet import delete_cart_by_id
from webapp.crud.cart.read import get_cart_by_user
from webapp.integrations.cache.cache import redis_set_products
from webapp.integrations.postgres import get_session


@cart_router.delete('/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_cart(
    product_id: int,
    access_token: Annotated[OAuth2PasswordRequestForm, Depends(oauth2_scheme)],
    session: AsyncSession = Depends(get_session),
) -> Response:

    user_id = get_user_id(access_token)

    cart = await delete_cart_by_id(session, product_id, user_id)

    if not cart:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    products = await get_cart_by_user(session, user_id)

    redis_product = await redis_set_products(user_id, products)

    print(redis_product)
