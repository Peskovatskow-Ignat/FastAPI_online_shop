from sqlalchemy.ext.asyncio import AsyncSession

from webapp.models.shop.product import Product
from webapp.schema.shop.product import ProductData


async def create_product(session: AsyncSession, product_data: ProductData, user_id: int):

    product = Product(**product_data.dict(), user_id=user_id)

    async with session.begin_nested():
        session.add(product)
        await session.flush()
        await session.commit()

    return product
