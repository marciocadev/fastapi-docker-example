from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import FastIn, FastOut, FastUpdate
from app.api import service

from devtools import debug

router = APIRouter()

@router.post('/', response_model=FastOut, status_code=201)
async def create_fast(payload: FastIn):
    fast_id = await service.create_fast(payload)

    response = {
        'id': fast_id,
        **payload.dict()
    }

    debug(response)
    return response