from pydantic import BaseModel


class UserPasswordChangeSchema(BaseModel):
    user_id: int
    old_password: str
    new_password: str
