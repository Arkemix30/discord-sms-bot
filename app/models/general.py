# isort: skip_file
# Python Imports
from datetime import datetime as dt
from typing import Optional

from sqlalchemy.ext.declarative import declared_attr

# Third party libraries
from sqlmodel import Field

# Local Imports
from app.utils.utils_models import class_name_to_lower

from .base import Base

tablename_base = "general_"


class Numbers(Base, table=True):
    number: str = Field(max_length=100)
    is_active: bool = True
    created_by: Optional[str] = Field(default=None, nullable=True)

    @declared_attr
    def __tablename__(cls):
        return tablename_base + class_name_to_lower(cls.__name__)


class Notifications(Base, table=True):
    message: str = Field(max_length=250)
    sent_at: Optional[dt] = Field(default=dt.utcnow(), nullable=True)
    sent_by: Optional[str] = Field(default=None, nullable=True)

    @declared_attr
    def __tablename__(cls):
        return tablename_base + class_name_to_lower(cls.__name__)


class NumbersNotifications(Base, table=True):
    number_id: Optional[int] = Field(
        default=None, foreign_key=f"{tablename_base}numbers.id", nullable=True
    )
    notification_id: Optional[int] = Field(
        default=None,
        foreign_key=f"{tablename_base}notifications.id",
        nullable=True,
    )

    @declared_attr
    def __tablename__(cls):
        return tablename_base + class_name_to_lower(cls.__name__)
