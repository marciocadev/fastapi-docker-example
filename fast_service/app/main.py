from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

router = APIRouter()

app = FastAPI(openapi_url="/api/v1/fast/openapi.json", docs_url="/api/v1/fast/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@router.get("/")
async def root():
    txt = {"message": "Hello"}
    return txt
    #{"message": "Hello World"}
    
app.include_router(router, prefix='/api/v1/fast', tags=['fast'])
