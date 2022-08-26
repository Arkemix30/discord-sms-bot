from sqlmodel import Session, create_engine

from app.core.config import get_db_uri

DATABASE_URI = get_db_uri()

engine = create_engine(DATABASE_URI, echo=True)


def get_session():
    return Session(engine)
