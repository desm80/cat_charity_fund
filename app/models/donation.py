from sqlalchemy import Column, Integer, ForeignKey, Text

from app.models.base_model import BaseAbstractModel


class Donation(BaseAbstractModel):
    user_id = Column(
        Integer,
        ForeignKey('user.id', name='fk_donation_user_id_user')
    )
    comment = Column(Text, nullable=True)

