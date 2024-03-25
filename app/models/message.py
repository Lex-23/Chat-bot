from beanie import Document
import datetime
from pydantic import Field
from typing import Optional, Union
from user import User
from chat import Chat

class Message(Document):
    user: User
    username: str
    text: str
    chat: Chat
    # type: str = Field(max_length=200)
    created_at: datetime.date = datetime.datetime.now()

    class Settings:
        name = "messages_database"
