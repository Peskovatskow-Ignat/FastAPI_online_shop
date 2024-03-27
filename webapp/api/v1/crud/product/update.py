from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from webapp.api.v1.crud.product.router import product_router
from webapp.auth.jwt import get_user_id, oauth2_scheme
from webapp.crud.product.update import update_product_by_id
from webapp.integrations.postgres import get_session
from webapp.schema.shop.product import ProductData, ProductResp


@product_router.put('/{product_id}', status_code=status.HTTP_200_OK, response_model=ProductResp)
async def update_user(
    product_id: int,
    user_info: ProductData,
    access_token: Annotated[OAuth2PasswordRequestForm, Depends(oauth2_scheme)],
    session: AsyncSession = Depends(get_session),
) -> ProductResp:

    user_id = get_user_id(access_token)

    try:
        product = await update_product_by_id(session, product_id, user_id, user_info)
    except Exception as ex:
        print(ex)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    return product
