import pwdlib
from fastapi import APIRouter
from ..database import SessionDep
from ..schemes.user import User as user_scheme
from ..models import User as user_model
from authority.encrypt import hasher

router = APIRouter(prefix="/auth")


@router.post("/login")
def login(user: user_scheme, session: SessionDep): 
    user_ = session.query(user_model).filter(user_model.name == user.name)
    return {"uuid": user_.first().uuid}
    


@router.post("/register")
def register(user: user_scheme, session: SessionDep):
    model_ = user_model(name=user.name, hashed_password=hasher.hash(user.password))
    session.add(model_)
    session.commit()
    return {"id": model_.uuid}
    
