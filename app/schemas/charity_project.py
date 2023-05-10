from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, PositiveInt, Extra, validator

TIME_EXAMPLE = datetime.now().isoformat(timespec='minutes')


class CharityProjectCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    full_amount: PositiveInt


class CharityProjectUpdate(CharityProjectCreate):
    name: str = Field(None, min_length=1, max_length=100)
    description: str = Field(None, min_length=1)
    full_amount: PositiveInt = Field(None)

    class Config:
        extra = Extra.forbid


class CharityProjectDB(CharityProjectCreate):
    id: int
    full_amount: PositiveInt
    invested_amount: int = 0
    fully_invested: bool
    create_date: datetime = Field(..., example=TIME_EXAMPLE)
    close_date: Optional[datetime] = Field(None, example=TIME_EXAMPLE)

    @validator('create_date', 'close_date')
    def date_to_isoformat(cls, value):
        if value is not None:
            return value.isoformat(timespec='minutes')

    class Config:
        orm_mode = True
