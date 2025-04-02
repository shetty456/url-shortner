from fastapi import FastAPI
from app.routes import urls
from app.database import init_db, close_db
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await close_db()


app = FastAPI(lifespan=lifespan)


app.include_router(urls.router)
