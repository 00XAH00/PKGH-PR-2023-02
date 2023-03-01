from typing import List
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from starlette import status
from src.models.schemas.cart_object_create import CartObjectCreateSchema
from src.models.schemas.cart_object_response import CartObjectResponse
from src.models.schemas.cart_object_update import CartObjectUpdate
from src.services.cart_objects import CartObjectService
from src.services.exception import ExceptionService
from src.services.users import UserService


router = APIRouter(
    prefix='/cart',
    tags=['cart']
)

oauth2_schema = OAuth2PasswordBearer(tokenUrl='/users/authorize')


def get_current_user_id(token: str = Depends(oauth2_schema), user_service: UserService = Depends()) -> int:
    return user_service.verify_token(token)


@router.post('/create_cart_object', response_model=CartObjectResponse, name="Добавление товара в корзину",
             status_code=status.HTTP_201_CREATED)
def create_cart_object(cart_object: CartObjectCreateSchema, cart_object_service: CartObjectService = Depends(),
                       user_service: UserService = Depends(), user_id: int = Depends(get_current_user_id),
                       exception_service: ExceptionService = Depends()):
    """
        Добавление товара в корзину
    """
    if not user_service.is_user_admin(user_id):
        exception_service.forbidden_error()

    return cart_object_service.create_cart_object(cart_object, user_id)


@router.delete('/remove_cart_object', name="Удаление товара из корзины", status_code=status.HTTP_204_NO_CONTENT)
def remove_cart_object(cart_object_id: int, cart_object_service: CartObjectService = Depends(),
                       user_service: UserService = Depends(), user_id: int = Depends(get_current_user_id),
                       exception_service: ExceptionService = Depends()):
    """
        Удаление товара из корзины
    """
    if not user_service.is_user_admin(user_id):
        exception_service.forbidden_error()

    return cart_object_service.remove_cart_object(cart_object_id)


@router.post('/get_user_cart', name="Получение списка товаров пользователя", response_model=List[CartObjectResponse])
def get_user_cart(cart_object_service: CartObjectService = Depends(), user_service: UserService = Depends(),
                  user_id: int = Depends(get_current_user_id), exception_service: ExceptionService = Depends()):
    """
        Получение корзины пользователя
    """
    if not user_service.is_user_admin(user_id):
        exception_service.forbidden_error()

    return cart_object_service.get_cart_objects_by_user_id(user_id)


@router.put('/change_cart_object_data', name='Обновление данных товара в корзине пользователя',
            response_model=CartObjectResponse)
def change_cart_object_data(cart_object_new_data: CartObjectUpdate, user_id: int = Depends(get_current_user_id),
                            user_service: UserService = Depends(), exception_service: ExceptionService = Depends(),
                            cart_object_service: CartObjectService = Depends()):
    """
        Обновление данных товара в корзине пользователя
    """
    if not user_service.is_user_admin(user_id):
        exception_service.forbidden_error()

    return cart_object_service.update_cart_object(cart_object_new_data)
