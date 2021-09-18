from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import Date, DateTime
from sqlalchemy_serializer import SerializerMixin
from database.database import Base
from datetime import datetime

class Scan(Base, SerializerMixin):
    __tablename__ = 'scans'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, unique=False, default=datetime.now)
    card_uid = Column(String, unique=False)
    currency_amount = Column(Integer, unique=False)

    def __init__(self, card_uid, currency_amount):
        self.card_uid = card_uid
        self.currency_amount = currency_amount

    def __repr__(self):
        return f'<User {self.name!r}>'