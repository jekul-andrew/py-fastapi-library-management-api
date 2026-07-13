from pydantic import BaseModel
from datetime import date


class AuthorBase(BaseModel):
    name: str
    bio: str


class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Config:
        orm_mod: True


class BookBase(BaseModel):
    title: str
    summary: str
    publication_date: date
    # author_id: int


class BookCreate(BookBase):
    author_id: int

class Book(BookBase):
    id: int
    author: Author

    class Config:
        orm_mode: True
