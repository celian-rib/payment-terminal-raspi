from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import Float
from database.database import Base
from sqlalchemy_serializer import SerializerMixin

class User(Base, SerializerMixin):
    __tablename__ = 'users'
    card_id = Column(String, primary_key=True, autoincrement=False)
    currency_amount = Column(Float, default=0)

    def __init__(self, card_id, currency_amount):
        self.card_id = card_id
        self.currency_amount = currency_amount

    def __repr__(self):
        return f'<User {self.name!r}>'
