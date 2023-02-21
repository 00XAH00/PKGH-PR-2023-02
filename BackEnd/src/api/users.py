from fastapi import APIRouter, Depends
from src.models.schemas.user_create import UserCreateSchema
from src.models.schemas.user_response import UserResponse
from src.services.users import UserService


router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.post('/create_user', response_model=UserResponse, name="Тестовый запрос")
def get(user: UserCreateSchema, user_service: UserService = Depends()):
    """

    """
    # user_password_first = user_service.password_hash("test_passwd")
    #
    # return user_service.password_check(input_password=user_password, user_password=user_password_first)
    return user_service.create_user(user)
