from sqlalchemy.orm import Session
from db import models
import schemas


def get_author_by_name(db: Session, name: str):
    return (
        db.query(
            models.DBAuthor
        ).filter(
            models.DBAuthor.name == name
        ).first()
    )


def get_all_authors(db: Session):
    return db.query(models.DBAuthor).all()


def create_author(
        db: Session,
        author: schemas.AuthorCreate
):
    db_author = models.DBAuthor(
        name=author.name,
        bio=author.bio
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_book_list(db: Session, author: str | None = None):
    queryset = db.query(models.DBBooks)

    if author is None:
        queryset = queryset.filter(models.DBBooks.author.has(name=author))

    return queryset.all()


def get_book(db: Session, book_id: int):
    return db.query(
        models.DBBooks
    ).filter(
        models.DBBooks.id == book_id
    ).first()


def get_book_by_title(db: Session, title: str):
    return db.query(
        models.DBBooks
    ).filter(
        models.DBBooks.title == title
    ).first()


def create_book(
        db: Session,
        book: schemas.BookCreate
):
    db_book = models.DBBooks(
        title = book.title,
        summary = book.summary,
        publication_date = book.publication_date,
        author_id = book.author_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
