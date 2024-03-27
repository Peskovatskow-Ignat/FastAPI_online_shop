from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from webapp.models.shop.product import Product


async def delete_product_by_id(session: AsyncSession, product_id: int, user_id: int):

    product = await session.scalar(select(Product).where(and_(Product.id == product_id, Product.user_id == user_id)))

    if product:
        await session.delete(product)
        await session.commit()
        return True

    return False
