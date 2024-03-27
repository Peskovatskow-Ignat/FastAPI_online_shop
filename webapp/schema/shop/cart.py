from pydantic import BaseModel, ConfigDict

from webapp.schema.shop.product import ProductResp


class CartData(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    product_id: int


class CartPesp(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int

    user_id: int

    product_id: int


class CartItem(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int

    product: ProductResp
