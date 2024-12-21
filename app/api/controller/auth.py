from tabnanny import check

from fastapi import HTTPException, status
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.api.repositories.auth import AuthRepository
from app.api.schemas.auth import UserInSchema
from passlib.hash import bcrypt


class AuthController:

    def __init__(self, auth_repo: AuthRepository = Depends()):
        self.__auth_repo = auth_repo

    async def create_user(self, data: UserInSchema):
        data.password = bcrypt.hash(data.password)
        return await self.__auth_repo.create_user(data=data.model_dump())

    async def check_user(self, data: OAuth2PasswordRequestForm) -> bool:
        user = self.__auth_repo.check_exist_user(data.username)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Not Authorized"
            )
        # todo: check password
