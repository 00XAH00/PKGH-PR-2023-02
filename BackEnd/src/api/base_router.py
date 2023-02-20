from fastapi import APIRouter
from src.api import users

router = APIRouter()
router.include_router(users.router)
