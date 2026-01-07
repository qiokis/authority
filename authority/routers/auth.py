import pwdlib
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from ..database import SessionDep
from ..schemes.user import User as user_scheme
from ..models import User as user_model
from ..schemes.token import Token
from ..utils.encrypt import hasher
from ..utils.encrypt import get_password_hash, verify_password_hash
from ..utils.jwt_util import get_jwt, decode_jwt, Payload, jwt_identify


router = APIRouter(prefix="/auth")


@router.post("/signin", response_model=Token)
def get_token(
        session: SessionDep,
        form_data: OAuth2PasswordRequestForm = Depends()
    ):
    user_ = session.query(user_model) \
        .filter(user_model.name == form_data.username).first()
    if user_ is None:
        return {"status": "not valid"}
    if verify_password_hash(form_data.password, user_.hashed_password) is False:
        return {"status": "not valid"}
    return {
        "access_token": get_jwt(Payload(username=user_.name)),
        "token_type": "Bearer"
    }


@router.post("/signup")
def register(user: user_scheme, session: SessionDep):
    try:
        model_ = user_model(
            name=user.name,
            hashed_password=get_password_hash(user.password)
        )
        session.add(model_)
        session.commit()
    except BaseException:
        return {"id": "null", "status": "Failed"}
    return {"id": model_.uuid, "status": "Success"}
