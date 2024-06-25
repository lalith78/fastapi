from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DATETIME_TIMEZONE,TIMESTAMP
from sqlalchemy.sql.expression import text

from .database import Base


class user(Base):
    __tablename__="users1"
    id=Column(Integer,primary_key=True,nullable=False)
    email=Column(String,nullable=False)
    password=Column(String,nullable=False)
 

class details(Base):
    __tablename__="user_details1"
    id=Column(Integer,primary_key=True,nullable=False)
    name=Column(String,nullable=False)
    age=Column(Integer,nullable=False)
    description=Column(String)
    createdat=Column(TIMESTAMP(timezone=True),nullable=False,server_default= text('now()'))
    user_id=Column(Integer,ForeignKey("users1.id",ondelete="CASCADE"),nullable=False)
    owner=relationship(user)

 