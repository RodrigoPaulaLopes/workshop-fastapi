from typing import Optional
from sqlmodel import Field, SQLModel
from pamps.security import HashedPassword
from pydantic import BaseModel


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, nullable=False)
    username: str = Field(unique=True, nullable=False)
    full_name: Optional[str] = None
    avatar: Optional[str] = None
    bio: Optional[str] = None
    password: str
    
    
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