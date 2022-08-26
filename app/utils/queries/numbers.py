from sqlmodel import Session, select

from app.models import Numbers
from app.schemas.register import RegisterSchema


def get_number(sessions: Session, existing_number: RegisterSchema):
    statement = select(Numbers).where(
        Numbers.number == existing_number.number
    )
    return sessions.exec(statement).one_or_none()


def get_all_active_numbers(sessions: Session):
    statement = select(Numbers).where(Numbers.is_active is True)
    return sessions.exec(statement).fetchall()
