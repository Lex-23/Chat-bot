from beanie import Document
import datetime
from pydantic import Field
from typing import Optional, Union

class User(Document):
    username: str = Field(max_length=100)
    created_at: datetime.date = datetime.date.today()
    is_active: bool = True
    chats: Optional[Union[list, None]]

    class Settings:
        name = "users_database"

    class Config:
        cshema_extra = {
            "username": "John",
            "created_at": datetime.date.today(),
            "is_active": True,
            "chats": []
        }