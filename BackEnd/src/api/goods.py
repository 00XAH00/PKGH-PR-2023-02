from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from starlette import status
from src.models.schemas.product_create import ProductCreateSchema
from src.models.schemas.product_response import ProductResponse
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
def create_product(product: ProductCreateSchema, product_service: ProductService = Depends()):
    """
        Добавление товара
    """
    return product_service.create_product(product)
