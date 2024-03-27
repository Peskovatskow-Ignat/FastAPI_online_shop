from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import DECIMAL, BigInteger, Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from webapp.models.enum.product import ProductEnum
from webapp.models.meta import DEFAULT_SCHEMA, Base

if TYPE_CHECKING:
    from webapp.models.shop.cart import Cart


class Product(Base):

    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)

    title: Mapped[str] = mapped_column(String)

    descriptions: Mapped[str] = mapped_column(String)

    price: Mapped[Decimal] = mapped_column(DECIMAL)

    photo: Mapped[str] = mapped_column(String)

    category: Mapped[str] = mapped_column(Enum(ProductEnum))

    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey(f'{DEFAULT_SCHEMA}.user.id'))

    cart: Mapped['Cart'] = relationship('Cart', back_populates='product')
