from pydantic import BaseModel,EmailStr
from typing import ClassVar


class userout(BaseModel):
    id:int
    email:EmailStr
    class config:
        orm_mode=True

class userout(BaseModel):
    id:int
    email:EmailStr
    class config:
        orm_mode=True

class post(BaseModel):
    name: str
    age:int
    description:str
      

    

class users(BaseModel):
    email: EmailStr
    password: str

class token(BaseModel):
    access_token:str
    token_type:str
class tokenid(BaseModel):
    id:int    

