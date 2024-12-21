from fastapi import APIRouter, Depends, HTTPException

from app.api.controller.rooms import RoomsController

router = APIRouter()


@router.get("/")
async def get_rooms(controller: RoomsController = Depends()):
    return await controller.get_rooms()


@router.get("/{room_id}")
async def get_room(controller: RoomsController = Depends(), room_id: int = None):
    if room_id is None:
        raise HTTPException(status_code=400, detail="Room ID is required")
    return await controller.get_room(room_id)
