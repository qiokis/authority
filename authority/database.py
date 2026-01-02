from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from typing import Annotated, Generator
from fastapi import Depends

from .models.base import BaseModel


engine = create_engine("")
BaseModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()

SessionDep = Annotated[Session, Depends(get_session)]
