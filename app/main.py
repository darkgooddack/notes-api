import logging

import uvicorn
from fastapi import FastAPI
from app.routers.router import v1 as api_router
from starlette.responses import RedirectResponse

import logging

logging.basicConfig(
    format="%(levelname)s - %(message)s",
    level=logging.INFO,
)

logging.info("✅ FastAPI запущен")

app = FastAPI()

app.include_router(api_router)

@app.get("/")
def read_root():
    logging.info("✅ Переадресация на Swagger")
    return RedirectResponse(url="/docs")

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )