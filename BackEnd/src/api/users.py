from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from starlette import status
from src.models.schemas.jwt import JWT
from src.models.schemas.user_create import UserCreateSchema
from src.models.schemas.user_response import UserResponse
from src.services.users import UserService


router = APIRouter(
    prefix='/users',
    tags=['users']
)

oauth2_schema = OAuth2PasswordBearer(tokenUrl='/users/authorize')


def get_current_user_id(token: JWT = Depends(oauth2_schema)) -> int:
    return UserService.verify_token(token)


@router.post('/create_user', response_model=UserResponse, name="Добавление пользователя")
def create_user(user: UserCreateSchema, user_service: UserService = Depends()):
    """
        Создание пользователя
    """
    return user_service.create_user(user)


@router.delete('/delete_user', response_model=UserResponse, name="Удаление пользователя", status_code=status.HTTP_204_NO_CONTENT)
def remove_user(remove_user_id: int, user_service: UserService = Depends(), main_user_id: int = Depends(get_current_user_id)):
    """
        Удаление пользователя
    """
    return user_service.remove(remove_user_id)


@router.put('/change_user_password')
def change_user_password(user_service: UserService = Depends()): ...


@router.post('/authorize', response_model=JWT, name="Авторизация пользователя")
def user_authorize(auth_schema: OAuth2PasswordRequestForm = Depends(), user_service: UserService = Depends()):
    result = user_service.authorize(auth_schema.username, auth_schema.password)

    return result


@router.get('/get_me', response_model=UserResponse, name="Получить пользователя")
def get_me(user_service: UserService = Depends(), user_id: int = Depends(get_current_user_id)):
    print(user_id)
