from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from webapp.models.shop.product import Product
from webapp.schema.shop.product import ProductData


async def update_product_by_id(
    session: AsyncSession, product_id: int, user_id: int, product_info: ProductData
) -> Product:

    product_to_update = await session.scalar(
        select(Product).where(and_(Product.id == product_id, Product.user_id == user_id))
    )

    if not product_to_update:
        product = Product(**product_info.dict(), user_id=user_id)
        async with session.begin_nested():
            session.add(product)
            await session.flush()
            await session.commit()
        return product

    product_info_dict = product_info.model_dump()
    for attr, val in product_info_dict.items():
        setattr(product_to_update, attr, val)

    await session.commit()
    return product_to_update
