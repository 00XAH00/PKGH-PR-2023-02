from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    first_name: str
    second_name: str
    phone: str
    email: str

    class Config:
        orm_mode = True
