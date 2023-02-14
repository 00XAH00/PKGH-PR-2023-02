from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = 'localhost'
    port: int = 9000
    connection_string: str


settings = Settings(
    _env_file="../.env",
    _env_file_encoding="utf-8"
)
