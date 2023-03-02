from pydantic import BaseModel


class CartObjectCreateSchema(BaseModel):
    count: int
    product_id: int
