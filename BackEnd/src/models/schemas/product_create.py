import json

from pydantic import BaseModel


class ProductCreateSchema(BaseModel):
    manufacture_name: str
    name: str
    price: int
    code: str
    description: json
    is_available: bool
