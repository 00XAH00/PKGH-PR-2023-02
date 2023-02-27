from fastapi import HTTPException
from starlette import status


class ExceptionService:

    @staticmethod
    def forbidden_error() -> None:
        error_details = "У вас не достаточно прав для выполнения данной операции"
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=error_details)

    @staticmethod
    def already_exist(exception_block_error: str) -> None:
        error_details = "Информация не доступна"
        if exception_block_error == "user":
            error_details = "Данный пользователь уже существует"
        if exception_block_error == "product":
            error_details = "Данный товар уже существует"

        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error_details)
