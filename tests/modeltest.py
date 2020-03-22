from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

MyBaseModel = declarative_base()


class User(MyBaseModel):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)

    fullname = Column(String(200))

    addressid = Column(Integer, ForeignKey('Addresses.id'))
    address = relationship("Address")


class Address(MyBaseModel):
    __tablename__ = "Addresses"

    id = Column(Integer, primary_key=True)

    street = Column(String(200), nullable=False)

    number = Column(Integer, nullable=False)

    neighborhood = Column(String(200), nullable=False)

    city = Column(String(200), nullable=False)

    country = Column(String(200), nullable=False)




