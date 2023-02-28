from pydantic import BaseModel


class ProductResponse(BaseModel):
    id: int
    manufacture_name: str
    name: str
    price: int
    code: str
    description: dict
    is_available: bool

    class Config:
        orm_mode = True
