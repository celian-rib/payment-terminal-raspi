from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin
from database.database import Base
from .public_data_filter import PublicDataFilter


class Product(Base, SerializerMixin, PublicDataFilter):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    price = Column(Integer, default=None)
    color = Column(String, default="#ffffff")
    asso_price = Column(Integer)

    def __init__(self, name, asso_price, color):
        self.name = name
        self.asso_price = asso_price
        self.color = color


class UserProductAssociation(Base, SerializerMixin, PublicDataFilter):
    __tablename__ = 'users_products'
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    count = Column(Integer, default=0)
    product = relationship(Product)
