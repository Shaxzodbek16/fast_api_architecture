from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.auth import UserInSchema
from app.core.database.config import get_general_session


class AuthRepository:

    def __init__(self, session: AsyncSession = Depends(get_general_session)):
        self.session = session

    async def create_user(self, data):
        stmt = text(
            """
        INSERT INTO users (username, password, first_name, last_name,  email, is_active,is_superuser, is_staff)
        VALUES (:username, :password, :first_name, :last_name, :email, :is_active, :is_superuser, :is_staff)
        """
        ).bindparams(**data)
        await self.session.execute(stmt)
        await self.session.commit()
        return UserInSchema.model_validate(data)
