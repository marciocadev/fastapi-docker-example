from app.api.models import FastIn, FastOut, FastUpdate
from app.api.db import database, fast

async def post(payload: FastIn):
    query = fast.insert().values(**payload.dict())
    return await database.execute(query=query)