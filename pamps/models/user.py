from typing import Optional
from sqlmodel import Field, SQLModel
from pamps.security import HashedPassword
from pydantic import BaseModel


class User(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, nullable=False)
    username: str = Field(unique=True, nullable=False)
    avatar: Optional[str] = None
    bio: Optional[str] = None
    password: HashedPassword
    
    
class UserRequest(BaseModel):
    email: str
    username: str
    password: str
    avatar: Optional[str] = None
    bio: Optional[str] = None

class UserResponse(BaseModel):
    username: str
    avatar: Optional[str] = None
    bio: Optional[str] = None