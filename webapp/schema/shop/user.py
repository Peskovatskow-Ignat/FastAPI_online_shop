from pydantic import BaseModel, ConfigDict

from webapp.models.enum.user import UserEnum


class UserData(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    email: str

    username: str

    password: str

    roll: UserEnum


class UserResp(BaseModel):

    model_config = ConfigDict(from_attributes=True, use_enum_values=True, arbitrary_types_allowed=True)

    id: int

    email: str

    username: str

    roll: UserEnum


class UserAuth(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    email: str

    password: str
