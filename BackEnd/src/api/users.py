from fastapi import APIRouter, Depends
from src.models.schemas.user_create import UserCreateSchema
from src.models.schemas.user_response import UserResponse
from src.services.users import UserService


router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.post('/create_user', response_model=UserResponse, name="Тестовый запрос")
def create_user(user: UserCreateSchema, user_service: UserService = Depends()):
    """
        Создание пользователя
    """
    return user_service.create_user(user)


# TODO: возвращать объект пользователя и результат его удаления
@router.delete('/delete_user', response_model=UserResponse, name="Удаление пользователя")
def remove_user(user_id: int, user_service: UserService = Depends()):
    """
        Создание пользователя
    """
    return user_service.remove(user_id)
