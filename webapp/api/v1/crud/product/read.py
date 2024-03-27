from typing import Annotated, List

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import parse_obj_as
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from webapp.api.v1.crud.product.router import product_router
from webapp.auth.jwt import get_user_id, oauth2_scheme
from webapp.crud.product.read import get_all_product, get_product_by_id, get_products_by_user
from webapp.integrations.postgres import get_session
from webapp.schema.shop.product import ProductResp


@product_router.get('', status_code=status.HTTP_200_OK, response_model=List[ProductResp])
async def get_user_product(
    access_token: Annotated[OAuth2PasswordRequestForm, Depends(oauth2_scheme)],
    session: AsyncSession = Depends(get_session),
) -> List[ProductResp]:
    user_id = get_user_id(access_token)

    product = await get_products_by_user(session, user_id)

    return parse_obj_as(List[ProductResp], product)


@product_router.get('s', status_code=status.HTTP_200_OK, response_model=List[ProductResp])
async def get_products(session: AsyncSession = Depends(get_session)) -> List[ProductResp]:
    products = await get_all_product(session)

    return parse_obj_as(List[ProductResp], products)


@product_router.get('/{product_id}', status_code=status.HTTP_200_OK, response_model=ProductResp)
async def get_product(
    product_id: int,
    session: AsyncSession = Depends(get_session),
) -> ProductResp:

    product = await get_product_by_id(session, product_id)

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return parse_obj_as(ProductResp, product)
