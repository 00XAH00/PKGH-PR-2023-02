import uvicorn
from src.core.settings import settings

if __name__ == "__main__":
    if settings.host:
        uvicorn.run(
            "app:app",
            host=settings.host,
            port=settings.port,
            reload=True
        )
    else:
        uvicorn.run(
            "app:app",
            port=settings.port,
            reload=True
        )
