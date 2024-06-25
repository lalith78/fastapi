from .routers import userdetails,users,auth
from .database import SessionLocal, engine
from . import models,schemas,database,utils
from fastapi import FastAPI


models.Base.metadata.create_all(bind=engine)


app=FastAPI()

app.include_router(users.router)
app.include_router(userdetails.router)
app.include_router(auth.router)