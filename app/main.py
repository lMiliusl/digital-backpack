from fastapi import FastAPI
from contextlib import asynccontextmanager

from core.database import engine
from vpn_monitor.models import Base
from vpn_monitor.router import router as vpn_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title="Digital Backpack API",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(vpn_router)

@app.get("/health")
async def health():
    return {"status": "ok"}