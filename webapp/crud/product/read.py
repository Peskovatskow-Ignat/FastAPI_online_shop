from typing import Any, Coroutine

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from webapp.models.shop.product import Product


async def get_all_product(sessions: AsyncSession) -> Coroutine[Any]:

    return (await sessions.scalars(select(Product))).all()


async def get_products_by_user(session: AsyncSession, user_id: int) -> Coroutine[Any]:

    return (await session.scalars(select(Product).where(Product.user_id == user_id))).all()


async def get_product_by_id(session: AsyncSession, product_id: int) -> Coroutine[Any]:

    return await session.get(Product, product_id)
