from fastapi import FastAPI
from src.api.base_router import router

tags = [
    {
        'name': 'categories',
        'description': 'Запросы для взаимодействия с категориями статей'
    },
    {
        'name': 'articles',
        'description': 'Запросы для взаимодействия со статьями'
    }
]

app = FastAPI(
    title="Example FastApi project",
    description="Project for learn FastApi And SQLAlchemy",
    version="0.1.0",
    openapi_tags=tags
)

app.include_router(router)
