from fastapi import FastAPI

from app.routers import versao

app = FastAPI()
app.include_router(versao.router)
