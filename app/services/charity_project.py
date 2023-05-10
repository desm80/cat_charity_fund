from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CharityProject


async def investment(
        charity_project: CharityProject,
        session: AsyncSession,
):
    pass
