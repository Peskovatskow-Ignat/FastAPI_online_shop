from typing import Any, Coroutine

from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from webapp.models.shop.cart import Cart


async def get_cart_by_user(session: AsyncSession, user_id: int) -> Coroutine:
    query = select(Cart).options(joinedload(Cart.product)).where(Cart.user_id == user_id)
    return (await session.execute(query)).scalars().all()


async def get_cart_by_id(session: AsyncSession, user_id: int, product_id: int) -> Coroutine:

    return await session.scalar(select(Cart).where(and_(Cart.product_id == product_id, Cart.user_id == user_id)))
