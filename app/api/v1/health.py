from fastapi import APIRouter
from sqlalchemy import text
from app.core.database import AsyncSessionLocal

router = APIRouter()

@router.get("")
async def health():
    async with AsyncSessionLocal() as session:
        await session.execute(text("SELECT 1"))
    return {"status": "healthy", "database": "connected"}
