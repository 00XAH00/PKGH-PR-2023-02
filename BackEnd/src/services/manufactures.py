from fastapi import Depends
from src.db.db import Session, get_session
from src.models.manufactures import Manufacture
from src.services.exception import ExceptionService


class ManufactureService:
    def __init__(self, session: Session = Depends(get_session), exception: ExceptionService = Depends()):
        self.session = session
        self.exception = exception

    def add_manufacture(self, manufacture_name: str) -> Manufacture:
        manufacture_name = manufacture_name[0].upper() + manufacture_name[1::].lower()
        if self.get_manufacture_by_name(manufacture_name):
            self.exception.already_exist("manufacture")
        manufacture = Manufacture(name=manufacture_name)

        self.session.add(manufacture)
        self.session.commit()
        return manufacture

    def get_manufacture_by_name(self, manufacture_name: str) -> Manufacture:
        manufacture_name = manufacture_name[0].upper() + manufacture_name[1::].lower()
        manufacture = (
            self.session.query(Manufacture)
            .filter(Manufacture.name == manufacture_name)
            .first()
        )

        return manufacture

    def remove_manufacture(self, manufacture_name: str) -> None:
        manufacture = self.get_manufacture_by_name(manufacture_name)
        if not manufacture:
            self.exception.not_exist_error("manufacture")

        self.session.delete(manufacture)
        self.session.commit()
