from pydantic import BaseModel
from src.models.schemas.product_response import ProductResponse


class CartObjectResponse(BaseModel):
    id: int
    count: int
    product: ProductResponse

    class Config:
        orm_mode = True
