from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.security import OAuth2PasswordBearer
from starlette import status
from starlette.background import BackgroundTasks
from src.services.exception import ExceptionService
from src.services.pictures import PictureService
from src.services.users import UserService


router = APIRouter(
    prefix='/pictures',
    tags=['pictures']
)

oauth2_schema = OAuth2PasswordBearer(tokenUrl='/users/authorize')


def get_current_user_id(token: str = Depends(oauth2_schema), user_service: UserService = Depends()) -> int:
    return user_service.verify_token(token)


@router.post('/create_picture', name="Добавление картинки товара",
             status_code=status.HTTP_201_CREATED)
def create_category(background_task: BackgroundTasks, product_code: str, picture: UploadFile = File(...),
                    picture_service: PictureService = Depends(), user_service: UserService = Depends(),
                    user_id: int = Depends(get_current_user_id), exception: ExceptionService = Depends()):
    """
        Добавление картинки товара
    """
    if not user_service.is_user_admin(user_id):
        exception.forbidden_error()

    background_task.add_task(picture_service.upload_picture, picture, product_code)

    picture_service.add_picture_in_database(product_code)

    # return picture_service.add_picture(product_code=product_code, picture=picture)
