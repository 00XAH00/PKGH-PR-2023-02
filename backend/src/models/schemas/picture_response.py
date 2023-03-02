from pydantic import BaseModel


class PictureResponse(BaseModel):
    id: int
    product_id: int
    url: str

    class Config:
        orm_mode = True
