from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import DateTime, Float
from database.database import Base
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

class User(Base, SerializerMixin):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    card_uid = Column(String, nullable=False)
    creation_date = Column(DateTime, default=datetime.now)
    update_date = Column(DateTime, default=None)
    currency_amount = Column(Integer, default=0)
    name = Column(String, default=None)
    first_name = Column(String, default=None)
    email = Column(String, default=None)

    def __init__(self, card_uid, currency_amount):
        self.card_uid = card_uid
        self.currency_amount = currency_amount

    def __repr__(self):
        return f'<User {self.name!r}>'
