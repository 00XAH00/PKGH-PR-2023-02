from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    first_name: str
    second_name: str
    phone: str
    email: str
    password: str
