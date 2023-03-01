from pydantic import BaseModel

from src.models.schemas.category_response import CategoryResponse
from src.models.schemas.manufacture_response import ManufactureResponse


class ProductResponse(BaseModel):
    id: int
    manufacture: ManufactureResponse
    category: CategoryResponse
    name: str
    price: int
    code: str
    description: str
    is_available: bool

    class Config:
        orm_mode = True
