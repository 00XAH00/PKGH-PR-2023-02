from typing import List, Union
from fastapi import Depends
from src.db.db import Session, get_session
from src.models.cart import Cart
from src.models.schemas.cart_object_create import CartObjectCreateSchema
from src.services.categories import CategoryService
from src.services.exception import ExceptionService
from src.services.manufactures import ManufactureService


class CartObjectService:
    def __init__(self, session: Session = Depends(get_session), exception_service: ExceptionService = Depends(),
                 manufacture_service: ManufactureService = Depends(),
                 category_service: CategoryService = Depends()):
        self.session = session
        self.manufacture = manufacture_service
        self.category = category_service
        self.exceptions = exception_service

    def create_cart_object(self, cart_object_new: CartObjectCreateSchema) -> Cart:
        cart_object = Cart(**cart_object_new.dict())

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
