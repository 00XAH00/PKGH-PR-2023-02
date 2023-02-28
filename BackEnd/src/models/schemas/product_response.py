from pydantic import BaseModel


class ProductResponse(BaseModel):
    id: int
    manufacture_id: int
    category_id: int
    name: str
    price: int
    code: str
    description: dict
    is_available: bool

    class Config:
        orm_mode = True
