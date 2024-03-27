from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from webapp.models.meta import DEFAULT_SCHEMA, Base

if TYPE_CHECKING:
    from webapp.models.shop.product import Product


class Cart(Base):

    __tablename__ = 'cart'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey(f'{DEFAULT_SCHEMA}.user.id'))

    product_id: Mapped[int] = mapped_column(BigInteger, ForeignKey(f'{DEFAULT_SCHEMA}.product.id'))

    product: Mapped['Product'] = relationship('Product', back_populates='cart')
