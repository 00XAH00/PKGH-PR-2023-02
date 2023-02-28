from typing import Optional, Union
from fastapi import Depends
from src.db.db import Session, get_session
from src.models.goods import Product
from src.models.schemas.product_create import ProductCreateSchema
from src.services.exception import ExceptionService


class ProductService:
    def __init__(self, session: Session = Depends(get_session), exception_service: ExceptionService = Depends()):
        self.session = session
        self.exceptions = exception_service

    def create_product(self, product_create: ProductCreateSchema) -> Product:
        product = Product(**product_create.dict())

        self.session.add(product)
        self.session.commit()

        return product
