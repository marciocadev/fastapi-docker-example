from app.api.models import FastIn, FastOut, FastUpdate
from app.api import db_manager

async def create_fast(payload: FastIn):
    return await db_manager.post(payload)
