from contextlib import asynccontextmanager
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware

from fastapi import FastAPI
from routes import router
from db import init_db

from auth import BasicAuthBackend
@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(
    lifespan=lifespan, 
    middleware=[Middleware(AuthenticationMiddleware, backend=BasicAuthBackend())]
    )


app.include_router(router)
