from pydantic import BaseModel, ConfigDict, validator

from webapp.models.enum.product import ProductEnum


class ProductData(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    title: str

    descriptions: str

    price: float

    photo: str

    category: ProductEnum

    @validator('price')
    @classmethod
    def parse_price(cls, val: int) -> int:
        if val <= 0:
            raise ValueError('The price must be greater than 0')
        return val


class ProductResp(BaseModel):

    model_config = ConfigDict(from_attributes=True, use_enum_values=True, arbitrary_types_allowed=True)

    id: int

    title: str

    descriptions: str

    price: float

    photo: str

    category: ProductEnum


class ProductItem(BaseModel):

    model_config = ConfigDict(from_attributes=True, use_enum_values=True, arbitrary_types_allowed=True)

    id: int

    product: ProductData
