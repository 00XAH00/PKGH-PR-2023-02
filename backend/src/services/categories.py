from typing import Union
from fastapi import Depends
from src.db.db import Session, get_session
from src.models.categories import Category
from src.services.exception import ExceptionService


class CategoryService:
    def __init__(self, session: Session = Depends(get_session), exception: ExceptionService = Depends()):
        self.session = session
        self.exception = exception

    def add_category(self, category_name: str) -> Category:
        category_name = category_name.lower()
        if category_name != "iphone":
            category_name = category_name[0].upper() + category_name[1::].lower()
        else:
            category_name = "iPhone"
        if self.get_category_by_name(category_name):
            self.exception.already_exist("category")
        category = Category(name=category_name)

        self.session.add(category)
        self.session.commit()
        return category

    def get_category_by_name(self, category_name: str) -> Union[Category, None]:
        category_name = category_name.lower()
        if category_name != "iphone":
            category_name = category_name[0].upper() + category_name[1::].lower()
        else:
            category_name = "iPhone"
        category = (
            self.session.query(Category)
            .filter(Category.name == category_name)
            .first()
        )

        return category

    def remove_category(self, category_name: str) -> None:
        category = self.get_category_by_name(category_name)
        if not category:
            self.exception.not_exist_error("category")

        self.session.delete(category)
        self.session.commit()
