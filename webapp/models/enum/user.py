from enum import Enum

from sqlalchemy.orm import Mapped


class UserEnum(Enum):

    buyer: Mapped[str] = 'byuer'

    seller: Mapped[str] = 'seller'
