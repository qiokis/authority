import jwt
from datetime import timedelta, datetime, UTC
from dataclasses import dataclass
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends
from ..database import SessionDep, Session

ENCODING_ALGORITHM: str = "HS256"
EXPIRITY_TIME: timedelta = timedelta(minutes=30)
_SECRET: str = "TESTTESST"
OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl="/auth/token")

class Payload(BaseModel):
    username: str


def get_jwt(payload: Payload) -> str:
    return jwt.encode(
        {
            **payload.dict(), 
            "exp": datetime.now(UTC) + EXPIRITY_TIME
        },
        _SECRET,
        algorithm=ENCODING_ALGORITHM
    )

def decode_jwt(token: str) -> Payload:
    return Payload(
        **jwt.decode(
            token, _SECRET,
            algorithm=ENCODING_ALGORITHM
        )
    )



def jwt_identify(
        token: str = Depends(OAUTH2_SCHEME)
    ) -> bool:
    try:
        payload = jwt.decode(token, _SECRET, algorithm=ALGORITHM)
        username: str = payload.get("username")
        if username is None:
            return False
    except BaseException:
        return False
    return True

