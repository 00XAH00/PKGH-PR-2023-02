from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from starlette import status
from src.models.schemas.product_change_price import ProductChangePriceSchema
from src.models.schemas.product_create import ProductCreateSchema
from src.models.schemas.product_response import ProductResponse
from src.services.exception import ExceptionService
from src.services.goods import ProductService
from src.services.users import UserService


router = APIRouter(
    prefix='/goods',
    tags=['goods']
)

oauth2_schema = OAuth2PasswordBearer(tokenUrl='/users/authorize')


def get_current_user_id(token: str = Depends(oauth2_schema), user_service: UserService = Depends()) -> int:
    return user_service.verify_token(token)


@router.post('/create_product', response_model=ProductResponse, name="Добавление товара",
             status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreateSchema, product_service: ProductService = Depends(),
                   user_service: UserService = Depends(), user_id: int = Depends(get_current_user_id),
                   exception_service: ExceptionService = Depends()):
    """
        Добавление товара
    """
    if not user_service.is_user_admin(user_id):
        exception_service.forbidden_error()

    return product_service.create_product(product)


@router.delete('/remove_product', name="Удаление товара", status_code=status.HTTP_204_NO_CONTENT)
def remove_product(product_code: str, product_service: ProductService = Depends(),
                   user_service: UserService = Depends(), user_id: int = Depends(get_current_user_id),
                   exception_service: ExceptionService = Depends()):
    """
        Удаление товара
    """
    if not user_service.is_user_admin(user_id):
        exception_service.forbidden_error()

    return product_service.remove_product(product_code)


@router.put('/change_product_price', name="Изменение цены товара", response_model=ProductResponse)
def change_product_price(product_price: ProductChangePriceSchema, product_service: ProductService = Depends(),
                         user_service: UserService = Depends(), user_id: int = Depends(get_current_user_id),
                         exception_service: ExceptionService = Depends()):
    """
        Изменение цены товара
    """
    if not user_service.is_user_admin(user_id):
        exception_service.forbidden_error()

    return product_service.change_product_price(product_price)


@router.get('/get_product', name="Получение товара", response_model=ProductResponse)
def get_product(product_code: str, product_service: ProductService = Depends(),
                exception_service: ExceptionService = Depends()):
    """
        Получение товара
    """
    product = product_service.get_product_by_code(product_code)
    if not product:
        exception_service.not_exist_error("goods")

    return product
