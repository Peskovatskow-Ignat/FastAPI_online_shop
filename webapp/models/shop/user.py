from sqlalchemy import BigInteger, Enum, String
from sqlalchemy.orm import Mapped, mapped_column

from webapp.models.enum.user import UserEnum
from webapp.models.meta import Base


class User(Base):

    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)

    email: Mapped[str] = mapped_column(String)

    username: Mapped[str] = mapped_column(String)

    password: Mapped[str] = mapped_column(String)

    roll: Mapped[str] = mapped_column(Enum(UserEnum))
