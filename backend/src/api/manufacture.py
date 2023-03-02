from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from starlette import status
from src.models.schemas.manufacture_response import ManufactureResponse
from src.services.exception import ExceptionService
from src.services.manufactures import ManufactureService
from src.services.users import UserService


router = APIRouter(
    prefix='/manufacture',
    tags=['manufacture']
)

oauth2_schema = OAuth2PasswordBearer(tokenUrl='/users/authorize')


def get_current_user_id(token: str = Depends(oauth2_schema), user_service: UserService = Depends()) -> int:
    return user_service.verify_token(token)


@router.post('/create_manufacture', response_model=ManufactureResponse, name="Добавление производителя",
             status_code=status.HTTP_201_CREATED)
def create_manufacture(manufacture_name: str, manufacture_service: ManufactureService = Depends(),
                       user_service: UserService = Depends(), user_id: int = Depends(get_current_user_id),
                       exception: ExceptionService = Depends()):
    """
        Добавление производителя
    """
    if not user_service.is_user_admin(user_id):
        exception.forbidden_error()

    return manufacture_service.add_manufacture(manufacture_name)


@router.delete('/create_manufacture', name="Удаление производителя", status_code=status.HTTP_204_NO_CONTENT)
def create_manufacture(manufacture_name: str, manufacture_service: ManufactureService = Depends(),
                       user_service: UserService = Depends(), user_id: int = Depends(get_current_user_id),
                       exception: ExceptionService = Depends()):
    """
        Удаление производителя
    """
    if not user_service.is_user_admin(user_id):
        exception.forbidden_error()

    return manufacture_service.remove_manufacture(manufacture_name)
