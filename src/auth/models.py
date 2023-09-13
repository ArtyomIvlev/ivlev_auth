
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String, Integer


class Base(DeclarativeBase):
    pass


metadata = Base.metadata


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(30))
    first_name: Mapped[str] = mapped_column(String(30))
    second_name: Mapped[Optional[str]]
    age: Mapped[int] = mapped_column(Integer)
    phone_number: Mapped[str] = mapped_column(String(10))
    current_course: Mapped[str] = mapped_column(String(10))
    joined_at: Mapped[Optional[str]]
    last_action: Mapped[Optional[str]]
    password: Mapped[str] = mapped_column(String(10))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, \
                name={self.first_name!r}, fullname={self.second_name!r})"
