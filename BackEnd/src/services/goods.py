from typing import Union

from fastapi import Depends
from src.db.db import Session, get_session
from src.models.goods import Product
from src.models.schemas.product_change_price import ProductChangePriceSchema
from src.models.schemas.product_create import ProductCreateSchema
from src.services.categories import CategoryService
from src.services.exception import ExceptionService
from src.services.manufactures import ManufactureService


class ProductService:
    def __init__(self, session: Session = Depends(get_session), exception_service: ExceptionService = Depends(),
                 manufacture_service: ManufactureService = Depends(),
                 category_service: CategoryService = Depends()):
        self.session = session
        self.manufacture = manufacture_service
        self.category = category_service
        self.exceptions = exception_service

    def create_product(self, product_create: ProductCreateSchema) -> Product:
        if self.get_product_by_name(product_create.name) or self.get_product_by_code(product_create.code):
            self.exceptions.already_exist("goods")

        manufacture = self.manufacture.get_manufacture_by_name(product_create.manufacture_name)
        if not manufacture:
            self.exceptions.not_exist_error("manufacture")
        manufacture_id = manufacture.id
        category = self.category.get_category_by_name(product_create.category_name)
        if not category:
            self.exceptions.not_exist_error("category")
        category_id = category.id
        product_create_dict: dict = product_create.dict()
        product_create_dict.pop("manufacture_name", None)
        product_create_dict.pop("category_name", None)
        product_create_dict.update({
            "category_id": category_id,
            "manufacture_id": manufacture_id
        })

        product = Product(**product_create_dict)

        self.session.add(product)
        self.session.commit()

        return product

    def remove_product(self, product_code: str) -> None:
        product = self.get_product_by_code(product_code)
        if not product:
            self.exceptions.not_exist_error("goods")

        self.session.delete(product)
        self.session.commit()

    def get_product_by_name(self, product_name: str) -> Union[Product, None]:
        product = (
            self.session.query(Product)
            .filter(Product.name == product_name)
            .first()
        )

        return product

    def get_product_by_code(self, product_code: str) -> Union[Product, None]:
        product = (
            self.session.query(Product)
            .filter(Product.code == product_code)
            .first()
        )

        return product

    def change_product_price(self, product_new_data: ProductChangePriceSchema) -> Product:
        product = self.get_product_by_code(product_new_data.product_code)
        if not product:
            self.exceptions.not_exist_error("goods")

        product.price = product_new_data.new_price
        self.session.commit()
        return product
