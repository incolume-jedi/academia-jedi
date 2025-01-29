import os
from typing import Optional

from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

DATABASE_URL = os.getenv('DATABASE_URL') or 'sqlite:////test.db'


class NotFoundError(Exception):
    pass


class Base(DeclarativeBase):
    pass


class DBItem(Base):
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]


class DBAutomation(Base):
    __tablename__ = 'automations'

    id: Mapped[int] = mapped_column(primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey('items.id'))
    code: Mapped[str]


engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


# Dependency to get the database session
def get_db():
    database = session_local()
    try:
        yield database
    finally:
        database.close()
