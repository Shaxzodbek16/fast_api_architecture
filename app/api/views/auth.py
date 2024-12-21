from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from app.api.controller.auth import AuthController
from app.api.schemas.auth import UserInSchema

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    data: UserInSchema,
    controller: AuthController = Depends(),
):
    return await controller.create_user(data=data)


@router.post("/token", status_code=status.HTTP_201_CREATED)
async def login_user():
    pass
