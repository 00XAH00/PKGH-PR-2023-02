from fastapi import Depends, UploadFile
from src.db.db import get_session, Session
from os import listdir, path, mkdir

from src.models.pictures import Picture
from src.services.exception import ExceptionService
from src.services.goods import ProductService


class PictureService:
    def __init__(self, session: Session = Depends(get_session), product_service: ProductService = Depends(),
                 exception_service: ExceptionService = Depends()):
        self.product = product_service
        self.session = session
        self.exception = exception_service

    def upload_picture(self, picture: UploadFile, product_code: str):
        picture_bytes = picture.file.read()
        path_to_file = f"./pictures/{product_code}"
        self.validate_path_and_create_path(path_to_file)

        result_path = f"{path_to_file}/{str(len(listdir(path_to_file))+1)+'.'+picture.filename.split('.')[-1]}"
        with open(result_path, 'wb') as f:
            f.write(picture_bytes)

    @staticmethod
    def validate_path_and_create_path(path_to_file: str):
        list_path_file = path_to_file.split('/')
        list_path_file = list_path_file[1::]

        current_path = "./"

        for i in list_path_file:
            dir_objects = listdir(current_path)

            if i not in dir_objects:
                mkdir(current_path+i)

            current_path += f"{i}/"

    def add_picture_in_database(self, product_code: str):
        product = self.product.get_product_by_code(product_code)
        if not product:
            self.exception.not_exist_error("goods")

        base_path = f"./pictures/{product_code}"
        pictures_count = len(listdir(base_path))
        for i in listdir(base_path):
            files_split_name = i.split('.')
            if pictures_count == int(files_split_name[0]):
                picture = Picture(url=f"{base_path}/{int(files_split_name[0])+1}.{files_split_name[1]}", product_id=product.id)

                self.session.add(picture)
                self.session.commit()
