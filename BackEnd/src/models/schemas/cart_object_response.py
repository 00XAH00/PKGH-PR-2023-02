from pydantic import BaseModel


class CartObjectResponse(BaseModel):
    id: int
    count: int
    user_id: int
    product_id: int

    class Config:
        orm_mode = True
