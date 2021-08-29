from sqlalchemy import Column, Integer, String
from database.database import Base
from sqlalchemy_serializer import SerializerMixin

class User(Base, SerializerMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, default=None)
    name = Column(String(50), unique=False, default=None)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User {self.name!r}>'
