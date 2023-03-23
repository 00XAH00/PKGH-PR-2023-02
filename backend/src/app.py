from fastapi import FastAPI
from src.api.base_router import router

tags = [
    {
        'name': 'users',
        'description': 'Запросы для взаимодействия с пользователями сайта'
    },
    {
        'name': 'goods',
        'description': 'Запросы для взаимодействия с товарами'
    },
    # {
    #     'name': 'reviews',
    #     'description': 'Запросы для взаимодействия с отзывами товаров'
    # },
    {
        'name': 'cart',
        'description': 'Запросы для взаимодействия с корзиной пользователя'
    },
    {
        'name': 'category',
        'description': 'Запросы для взаимодействия с категориями'
    },
    {
        'name': 'manufacture',
        'description': 'Запросы для взаимодействия с производителями'
    }
]

app = FastAPI(
    title="FastApi for AppleDevices shop",
    version="0.1.0",
    openapi_tags=tags
)

app.include_router(router)
