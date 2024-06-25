from fastapi import Depends, FastAPI, HTTPException,status,Response, APIRouter
from sqlalchemy.orm import Session
from .. import models,schemas,utils
from ..database import get_db
from typing import List

router=APIRouter(
    prefix="/users",tags=["users"]
)
router

@router.post("",status_code=status.HTTP_201_CREATED,response_model=schemas.userout)
def createuser(post:schemas.users,db:Session=Depends(get_db)):

    hashed_pass=utils.hash(post.password)
    post.password=hashed_pass

    new_info=models.user(**post.dict())
    db.add(new_info)
    db.commit()
    db.refresh(new_info)
    return new_info

@router.get("",response_model=list[schemas.userout])
def getuser(db:Session=Depends(get_db)):
    user=db.query(models.user).all()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"details with id:{id} was not found")
    return user

    
@router.get("/{id}",response_model=schemas.userout)
def getuser(id,post:schemas.users,db:Session=Depends(get_db)):
    user=db.query(models.user).filter(models.user.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"details with id:{id} was not found")
    return user
