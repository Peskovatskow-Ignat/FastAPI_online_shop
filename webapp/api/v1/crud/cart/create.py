from typing import Annotated, Any

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from webapp.api.v1.crud.cart.router import cart_router
from webapp.auth.jwt import get_user_id, oauth2_scheme
from webapp.crud.cart.create import create_cart
from webapp.crud.cart.read import get_cart_by_id, get_cart_by_user
from webapp.integrations.cache.cache import redis_set_products
from webapp.integrations.postgres import get_session
from webapp.schema.shop.cart import CartData, CartPesp


@cart_router.post('', status_code=status.HTTP_201_CREATED, response_model=CartPesp)
async def create(
    body: CartData,
    access_token: Annotated[OAuth2PasswordRequestForm, Depends(oauth2_scheme)],
    session: AsyncSession = Depends(get_session),
) -> dict[str, Any]:

    user_id = get_user_id(access_token)

    if await get_cart_by_id(session, user_id, body.dict().get('product_id', None)):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)

    try:

        product = await create_cart(session, body, user_id)

        products = await get_cart_by_user(session, user_id)

        await redis_set_products(user_id, products)

    except Exception as ex:
        print(ex)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    return product
