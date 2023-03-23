from pydantic import BaseModel


class ManufactureResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
