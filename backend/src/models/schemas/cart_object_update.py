from pydantic import BaseModel


class CartObjectUpdate(BaseModel):
    id: int
    count: int
