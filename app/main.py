import uvicorn
from fastapi import FastAPI
from app.routers.router import v1 as api_router  # Импортируем именно router, а не весь модуль
from starlette.responses import RedirectResponse

app = FastAPI()

app.include_router(api_router)

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )