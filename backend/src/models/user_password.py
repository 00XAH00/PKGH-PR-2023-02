from dataclasses import dataclass


@dataclass
class UserPassword:
    password: bytes
    salt: bytes
