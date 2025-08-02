from fastapi import FastAPI, Depends, HTTPException
from app.schemas import ProductCreate, ProductResponse
from app.database import get_async_session
from app import crud
from typing import List

app = FastAPI()

@app.post("/products", response_model=ProductResponse)
async def create_product(product: ProductCreate, session=Depends(get_async_session)):
    db_product = await crud.create_product(session, product)
    if not db_product:
        raise HTTPException(status_code=400, detail="Product could not be created.")
    return db_product

@app.get("/products", response_model=List[ProductResponse])
async def list_products(session=Depends(get_async_session)):
    return await crud.get_all_products(session)
