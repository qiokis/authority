from sqlalchemy.sql.sqltypes import UUID
from pydantic import BaseModel


class User(BaseModel):
    name: str
    password: str
