from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Donation


async def investment(
        donation: Donation,
        session: AsyncSession,
):
    pass
