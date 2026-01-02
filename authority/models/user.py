from .base import BaseModel
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
import uuid


class User(BaseModel):
    __tablename__ = "user"

    uuid: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name: Mapped[str] = mapped_column(String[30])
    hashed_password: Mapped[str] = mapped_column(String)
