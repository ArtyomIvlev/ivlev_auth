from datetime import datetime
from typing import Optional

import uuid

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


metadata = Base.metadata


class DefaultBase(Base):
    __abstract__ = True

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)

    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(insert_default=func.now())


class User(DefaultBase):
    __tablename__ = "user"

    email: Mapped[str] = mapped_column(String(30), unique=True, index=True)
    password: Mapped[str] = mapped_column(String(10))

    profiles: Mapped["Profile"] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, email={self.email!r})"


class Profile(DefaultBase):
    __tablename__ = "profile"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id"))
    first_name: Mapped[Optional[str]]
    second_name: Mapped[Optional[str]]
    age: Mapped[Optional[int]] = mapped_column(Integer)
    phone_number: Mapped[Optional[str]] = mapped_column(String(10))
    current_course: Mapped[Optional[str]] = mapped_column(String(10))

    user: Mapped["User"] = relationship(back_populates="profiles")

    def __repr__(self) -> str:
        return (f"Profile(id={self.id!r}, "
                f"first name={self.first_name!r}, second name={self.second_name!r})")
