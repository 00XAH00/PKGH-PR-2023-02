from fastapi import APIRouter
from src.api import users, goods, manufacture, category, cart_objects, picture

router = APIRouter()
router.include_router(users.router)
router.include_router(goods.router)
router.include_router(manufacture.router)
router.include_router(category.router)
router.include_router(cart_objects.router)
router.include_router(picture.router)
