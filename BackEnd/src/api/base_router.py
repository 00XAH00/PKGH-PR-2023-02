from fastapi import APIRouter
from src.api import users, goods, manufacture, category

router = APIRouter()
router.include_router(users.router)
router.include_router(manufacture.router)
router.include_router(category.router)
