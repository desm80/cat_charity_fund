from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


# Создаем новый класс, унаследованный от CRUDBase.
class CRUDCharityProject(CRUDBase):

    # # Преобразуем функцию в метод класса.
    # async def get_room_id_by_name(
    #         # Дописываем параметр self.
    #         # В качестве альтернативы здесь можно
    #         # применить декоратор @staticmethod.
    #         self,
    #         room_name: str,
    #         session: AsyncSession,
    # ) -> Optional[int]:
    #     db_room_id = await session.execute(
    #         select(MeetingRoom.id).where(
    #             MeetingRoom.name == room_name
    #         )
    #     )
    #     db_room_id = db_room_id.scalars().first()
    #     return db_room_id
    pass


charity_project_crud = CRUDCharityProject(CharityProject)
