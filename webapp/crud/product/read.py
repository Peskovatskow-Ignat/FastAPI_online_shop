from typing import Coroutine, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from webapp.models.shop.product import Product


async def get_all_product(sessions: AsyncSession) -> Sequence:

    return (await sessions.scalars(select(Product))).all()


async def get_products_by_user(session: AsyncSession, user_id: int):

    return (await session.scalars(select(Product).where(Product.user_id == user_id))).all()


async def get_product_by_id(session: AsyncSession, product_id: int) -> Coroutine:

    return await session.get(Product, product_id)
