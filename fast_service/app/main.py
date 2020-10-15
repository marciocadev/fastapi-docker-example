from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from app.api import fast
from app.api.db import database, engine, metadata

from devtools import debug


metadata.create_all(engine)

# router = APIRouter()

app = FastAPI(openapi_url="/api/v1/fast/openapi.json", docs_url="/api/v1/fast/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


# @router.get("/")
# async def root():
#     debug("Entrou no get")
#     return {"message": "Hello World"}
    
@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(fast.router, prefix='/api/v1/fast', tags=['fast'])
