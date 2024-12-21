from fastapi.params import Depends

from app.api.repositories.auth import AuthRepository
from app.api.schemas.auth import UserInSchema
from passlib.hash import bcrypt


class AuthController:

    def __init__(self, auth_repo: AuthRepository = Depends()):
        self.__auth_repo = auth_repo

    async def create_user(self, data: UserInSchema):
        data.password = bcrypt.hash(data.password)
        return await self.__auth_repo.create_user(data=data.model_dump())
