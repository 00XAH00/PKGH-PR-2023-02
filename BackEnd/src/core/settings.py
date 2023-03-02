from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = 'localhost'
    port: int = 9000
    connection_string: str
    password_hash_algorithm: str
    password_encoding: str
    jwt_time_expire_seconds: int
    jwt_secret: str
    jwt_algorithm: str


settings = Settings(
    _env_file=".env",
    _env_file_encoding="utf-8"
)
