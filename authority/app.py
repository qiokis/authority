from .routers import (
        auth_router
)

from fastapi import FastAPI

from .database import SessionDep


app = FastAPI()

app.include_router(auth_router)
