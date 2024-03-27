from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from webapp.models.shop.cart import Cart


async def delete_cart_by_id(session: AsyncSession, product_id: int, user_id: int) -> bool:

    product = await session.scalar(select(Cart).where(and_(Cart.product_id == product_id, Cart.user_id == user_id)))

    if product:
        await session.delete(product)
        await session.commit()
        return True

    return False
