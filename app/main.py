from contextlib import asynccontextmanager
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from fastapi.responses import JSONResponse

from fastapi import FastAPI
from api import router
from db import init_db

from auth import BasicAuthBackend


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(
    debug=True,
    lifespan=lifespan, 
    middleware=[
        Middleware(
            AuthenticationMiddleware, 
            backend=BasicAuthBackend(),
            on_error=lambda conn, exc: JSONResponse({"detail": str(exc)}, status_code=401)
            )
        ]
    )


app.include_router(router)
