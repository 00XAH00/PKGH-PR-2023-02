from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from starlette import status
from src.models.schemas.manufacture_response import ManufactureResponse
from src.services.categories import CategoryService
from src.services.exception import ExceptionService
from src.services.users import UserService


router = APIRouter(
    prefix='/category',
    tags=['category']
)

oauth2_schema = OAuth2PasswordBearer(tokenUrl='/users/authorize')


def get_current_user_id(token: str = Depends(oauth2_schema), user_service: UserService = Depends()) -> int:
    return user_service.verify_token(token)


@router.post('/create_category', response_model=ManufactureResponse, name="Добавление категории",
             status_code=status.HTTP_201_CREATED)
def create_category(category_name: str, category_service: CategoryService = Depends(),
                    user_service: UserService = Depends(), user_id: int = Depends(get_current_user_id),
                    exception: ExceptionService = Depends()):
    """
        Добавление категории
    """
    if not user_service.is_user_admin(user_id):
        exception.forbidden_error()

    return category_service.add_category(category_name)


@router.delete('/create_category', name="Удаление категории", status_code=status.HTTP_204_NO_CONTENT)
def create_category(category_name: str, category_service: CategoryService = Depends(),
                    user_service: UserService = Depends(), user_id: int = Depends(get_current_user_id),
                    exception: ExceptionService = Depends()):
    """
        Удаление категории
    """
    if not user_service.is_user_admin(user_id):
        exception.forbidden_error()

    return category_service.remove_category(category_name)
