from pydantic import BaseModel
from typing import List, Optional

class FastIn(BaseModel):
    name: str
    nationality: Optional[str] = None

class FastOut(FastIn):
    id: int

    class Config:
        schema_extra = {
            "example": {
                "id": "Unique identifier",
                "name": "Fast name",
                "nationality": "Fast nationality"
            }
        }

class FastUpdate(FastIn):
    name: Optional[str] = None