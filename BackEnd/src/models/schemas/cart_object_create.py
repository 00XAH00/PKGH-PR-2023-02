from pydantic import BaseModel


class CartObjectCreateSchema(BaseModel):
    count: int
    user_id: int
    product_id: int
