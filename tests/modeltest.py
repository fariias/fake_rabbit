from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base

MyBaseModel = declarative_base()


class User(MyBaseModel):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)

    fullname = Column(String(200))

