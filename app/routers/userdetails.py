from fastapi import Depends, FastAPI, HTTPException,status,Response,APIRouter
from sqlalchemy.orm import Session
from .. import models,schemas,utils,oauth2
from ..schemas import post,userout,users
from ..database import get_db
from ..oauth2 import get_current_user,verify_access_token
from typing import List

router=APIRouter(
    prefix="/details",tags=["details"]
)


@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.get("",response_model=List[schemas.post])
def get_details(db:Session=Depends(get_db),user_id:int=Depends(oauth2.get_current_user)):
    info=db.query(models.details).filter(models.details.user_id==user_id.id).all()

    return info
@router.get("/{id}")
def get_details(id:int,db:Session=Depends(get_db),user_id:int=Depends(oauth2.get_current_user)):
    info=db.query(models.details).filter(models.details.id==id).first()
    if not info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"details with id:{id} was not found")
    if user_id.id != info.user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"not authorized")

    
    return {"details":info}


@router.post("/post",status_code=status.HTTP_201_CREATED)
def post_details(post:post,db:Session=Depends(get_db),user_id1:int=Depends(oauth2.get_current_user)):
    print(user_id1.id)
    new_info=models.details(user_id=user_id1.id,**post.dict())
    db.add(new_info)
    db.commit()
    db.refresh(new_info)
    return{"details":new_info}

@router.put("/{id}")
def update_details(id,post1:post,db:Session=Depends(get_db),user_id:int=Depends(oauth2.get_current_user)):
    new_info=db.query(models.details).filter(models.details.id==id)
    post=new_info.first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"details with id:{id} was not found")
    if post.user_id != user_id.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"not authorized")

    new_info.update(post1.dict(),synchronize_session=False)
    post=new_info.first()
    db.commit()
    return {"details":new_info.first()}
    
@router.delete("/{id}")
def delete_details(id,db:Session=Depends(get_db),user_id:int=Depends(oauth2.get_current_user)):
    info1=db.query(models.details).filter(models.details.id==id)
    print(info1)

    info=info1.first()
    print
    if not info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"details with id:{id} was not found")
    if info.user_id != user_id.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"not authorized")


    info1.delete()
 
    db.commit()
    #db.refresh(info)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
