from pydantic import BaseModel


class ProductCreateSchema(BaseModel):
    manufacture_name: str
    category_name: str
    name: str
    price: int
    code: str
    description: str
    is_available: bool
