from pydantic import BaseModel, Field
from typing import Optional

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=128)
    description: Optional[str] = Field(default=None, max_length=512)
    quantity: int = Field(..., ge=0)
    price: float = Field(..., ge=0.0)

class ProductResponse(ProductCreate):
    id: int
    created_at: str
    class Config:
        orm_mode = True
