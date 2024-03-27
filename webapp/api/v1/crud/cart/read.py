from typing import Annotated, List

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import parse_obj_as
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from webapp.api.v1.crud.cart.router import cart_router
from webapp.auth.jwt import get_user_id, oauth2_scheme
from webapp.crud.cart.read import get_cart_by_user
from webapp.integrations.cache.cache import redis_get, redis_set_products
from webapp.integrations.postgres import get_session
from webapp.schema.shop.cart import CartItem


@cart_router.get('', status_code=status.HTTP_200_OK, response_model=List[CartItem])
async def get_user_product(
    access_token: Annotated[OAuth2PasswordRequestForm, Depends(oauth2_scheme)],
    session: AsyncSession = Depends(get_session),
):

    user_id = get_user_id(access_token)
    products = await redis_get(user_id)
    print(products)
    if not products:
        cart = await get_cart_by_user(session, user_id)
        if not cart:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        products = await redis_set_products(user_id, cart)

    return parse_obj_as(List[CartItem], products)
