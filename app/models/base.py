from datetime import datetime as dt
from typing import Optional

from sqlalchemy import func
from sqlmodel import Column, DateTime, Field, SQLModel


class Base(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: Optional[dt] = Field(
        sa_column=Column(
            DateTime(timezone=True), nullable=True, server_default=func.now()
        )
    )
    updated_at: Optional[dt] = Field(
        sa_column=Column(
            DateTime(timezone=True), nullable=True, onupdate=func.now()
        )
    )
