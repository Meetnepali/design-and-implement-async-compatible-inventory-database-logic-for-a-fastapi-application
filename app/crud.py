from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from app.models import Product
from app.schemas import ProductCreate
from sqlalchemy.ext.asyncio import AsyncSession

async def create_product(session: AsyncSession, product: ProductCreate):
    db_product = Product(
        name=product.name,
        description=product.description,
        quantity=product.quantity,
        price=product.price
    )
    session.add(db_product)
    try:
        await session.commit()
        await session.refresh(db_product)
        return db_product
    except IntegrityError:
        await session.rollback()
        return None

async def get_all_products(session: AsyncSession):
    result = await session.execute(select(Product))
    return result.scalars().all()
