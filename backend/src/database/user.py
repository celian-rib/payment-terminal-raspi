from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import DateTime, Float
from database.database import Base
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

class User(Base, SerializerMixin):
    __tablename__ = 'users'
    card_id = Column(String, primary_key=True, autoincrement=False)
    creation_date = Column(DateTime, default=datetime.now)
    currency_amount = Column(Float, default=0)
    name = Column(String, default=None)
    first_name = Column(String, default=None)
    email = Column(String, default=None)

    def __init__(self, card_id, currency_amount):
        self.card_id = card_id
        self.currency_amount = currency_amount

    def __repr__(self):
        return f'<User {self.name!r}>'
