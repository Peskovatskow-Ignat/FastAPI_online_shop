from enum import Enum

from sqlalchemy.orm import Mapped


class ProductEnum(Enum):

    electronic: Mapped[str] = 'electronic'

    household_goods: Mapped[str] = 'household_goods'

    meal: Mapped[str] = 'meal'
