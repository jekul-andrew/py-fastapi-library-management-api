from enum import StrEnum, auto
from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base

# class PackagingType(StrEnum):
#     IN_PACKAGE = auto()
#     WEIGHT = auto()

# books(relationship with the 'Book' model, one-to-many)

class DBAuthor(Base):

    __tablename__ = "author"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(225), nullable=False, unique=True)
    bio = Column(String(511), nullable=False)


class DBBooks(Base):

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(225), nullable=False, unique=True)
    summary = Column(String(511), nullable=False)
    publication_date = Column(Date, nullable=True)
    author_id = Column(Integer, ForeignKey("author.id"))
    author = relationship(DBAuthor)
