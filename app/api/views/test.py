from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.core.database.config import get_general_session

router = APIRouter()


@router.get("/test")
async def test(
    session: AsyncSession = Depends(get_general_session),
):
    test_sql = text("SELECT * FROM employee")
    result = await session.execute(test_sql)
    result = result.mappings().all()
    return result
