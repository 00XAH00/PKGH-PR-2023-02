from typing import List, Union
from fastapi import Depends
from src.db.db import Session, get_session
from src.models.cart import Cart
from src.models.schemas.cart_object_create import CartObjectCreateSchema
from src.models.schemas.cart_object_update import CartObjectUpdate
from src.services.categories import CategoryService
from src.services.exception import ExceptionService
from src.services.goods import ProductService
from src.services.manufactures import ManufactureService


class CartObjectService:
    def __init__(self, session: Session = Depends(get_session), exception_service: ExceptionService = Depends(),
                 manufacture_service: ManufactureService = Depends(), category_service: CategoryService = Depends(),
                 product_service: ProductService = Depends()):
        self.session = session
        self.manufacture = manufacture_service
        self.category = category_service
        self.exceptions = exception_service
        self.products = product_service

    def create_cart_object(self, cart_object_new: CartObjectCreateSchema, user_id: int) -> Cart:
        cart_object = self.get_cart_object_by_product_id_and_user_id(
            product_id=cart_object_new.product_id,
            user_id=user_id
        )
        if not cart_object:
            if not self.products.get_product_by_id(cart_object_new.product_id):
                self.exceptions.not_exist_error("goods")

            cart_object = Cart(**cart_object_new.dict(), user_id=user_id)

            self.session.add(cart_object)
            self.session.commit()

        return cart_object

    def get_cart_object_by_id(self, cart_object_id: int) -> Union[Cart, None]:
        cart_object = (
            self.session.query(Cart)
            .filter(Cart.id == cart_object_id)
            .first()
        )

        return cart_object

    def get_cart_objects_by_user_id(self, user_id: int) -> List[Cart]:
        user_cart_objects = (
            self.session.query(Cart)
            .filter(Cart.user_id == user_id)
            .all()
        )

        return user_cart_objects

    def remove_cart_object(self, cart_object_id: int) -> None:
        cart_object = self.get_cart_object_by_id(cart_object_id)

        if not cart_object:
            self.exceptions.not_exist_error("cart_object")

        self.session.delete(cart_object)
        self.session.commit()

    def update_cart_object(self, cart_object_new_data: CartObjectUpdate) -> Cart:
        cart_object = self.get_cart_object_by_id(cart_object_new_data.id)

        if not cart_object:
            self.exceptions.not_exist_error("cart_object")

        cart_object.count = cart_object_new_data.count

        self.session.commit()
        return cart_object

    def get_cart_object_by_product_id_and_user_id(self, product_id: int, user_id: int) -> Union[Cart, None]:
        cart_object = (
            self.session.query(Cart)
            .filter(
                Cart.product_id == product_id,
                Cart.user_id == user_id
            )
            .first()
        )

        return cart_object
