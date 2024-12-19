from fastapi.params import Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from app.api.schemas.rooms import RoomsSchema
from app.core.database.config import get_general_session


class RoomsRepository:
    def __init__(self, session: AsyncSession = Depends(get_general_session)):
        self.session = session

    async def get_all_rooms(self):
        raw_sql = text("""
        select m.room_number,s.title as room_type, m.price, f.title as status
        from rooms as m
        join rooms_status as f on m.status = f.id
        join rooms_type as s on m.room_type = s.id;
        """)
        stmt = await self.session.execute(raw_sql)
        return [RoomsSchema.model_validate(map_res) for map_res in stmt.mappings().all()]

    async def get_room(self, room_id: int):
        raw_sql = text("""
        select m.room_number,s.title as room_type, m.price, f.title as status
        from rooms as m
        join rooms_status as f on m.status = f.id
        join rooms_type as s on m.room_type = s.id
        where m.id = :room_id;
        """)
        stmt = await self.session.execute(raw_sql, {"room_id": room_id})
        result = stmt.mappings().first()
        if not result:
            raise HTTPException(status_code=404, detail="Room not found")
        return RoomsSchema.model_validate(result).model_dump()
