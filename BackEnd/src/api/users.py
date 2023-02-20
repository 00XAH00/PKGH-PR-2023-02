from fastapi import APIRouter, Depends
from src.services.users import UserService


router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get('/all', name="Тестовый запрос")
def get(user_password: str, user_service: UserService = Depends()) -> bool:
    """

    """
    user_password_first = user_service.password_hash("test_passwd")

    return user_service.password_check(input_password=user_password, user_password=user_password_first)
    # return categories_service.all()
