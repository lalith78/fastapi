from fastapi import FastAPI,APIRouter,Depends,status,HTTPException,Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import session
from .. import database,schemas,models,utils,oauth2
from ..database import get_db






router=APIRouter(
    tags=["authentication"]
)


#@router.post("/login")
#def login(user_cred:schemas.users,db:session=Depends(get_db)):
#    user=db.query(models.user).filter(models.user.email == user_cred.email).first()
#    if not user:
#       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid credentials")
#   if not utils.verify(user_cred.password,user.password):
#       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid credentials")
#   access_token=oauth2.create_access_token(data={"user_id":user.id})
#   return access_token

@router.post("/login",response_model=schemas.token)
def login(user_cred:OAuth2PasswordRequestForm=Depends(),db:session=Depends(get_db)):
    user=db.query(models.user).filter(models.user.email == user_cred.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid credentials")
    if not utils.verify(user_cred.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid credentials")
    access_token=oauth2.create_access_token(data={"user_id":user.id})
    return {"access_token": access_token, "token_type": "bearer"}





