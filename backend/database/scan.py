from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import Date, DateTime
from database.database import Base
from datetime import datetime

class Scan(Base):
    __tablename__ = 'scans'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, unique=False, default=datetime.now)
    card_id = Column(String, unique=False)
    currency_amount = Column(Integer, unique=False)

    def __init__(self, card_id, currency_amount):
        self.card_id = card_id
        self.currency_amount = currency_amount

    def __repr__(self):
        return f'<User {self.name!r}>'