from sqlalchemy.ext.asyncio import AsyncSession

from webapp.models.shop.cart import Cart
from webapp.schema.shop.cart import CartData


async def create_cart(session: AsyncSession, cart_data: CartData, user_id: int) -> CartData:

    cart = Cart(**cart_data.dict(), user_id=user_id)

    async with session.begin_nested():
        session.add(cart)
        await session.flush()
        await session.commit()

    return cart
