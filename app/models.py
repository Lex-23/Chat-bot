from __future__ import annotations
from beanie import Document
import datetime
from pydantic import Field
from typing import Optional, Union, List


class User(Document):
    username: str = Field(max_length=100)
    created_at: datetime.date = datetime.date.today()
    is_active: bool = True
    chats: Optional[Union[List[Chat], None]]

    class Settings:
        name = "users_database"

    class Config:
        json_schema_extra = {
            "username": "John",
            "created_at": datetime.date.today(),
            "is_active": True,
            "chats": []
        }


class Chat(Document):
    name: str = Field(max_length=200)
    type: str = Field(max_length=200)
    owner_username: str = Field(max_length=100)
    owner: User
    messages: Optional[Union[List[Message], None]]
    created_at: datetime.date = datetime.datetime.now()
    updated_at: datetime.date = datetime.datetime.now()
    is_active: bool = True
    type: str
    last_message: Message

    class Settings:
        name = "chats_database"


class ChatBot(Chat):
    purpose: str
    description: str = Field(max_length=1000)
    prescription: str = Field(max_length=1000)
    communicative_style: str = Field(max_length=500)

    class Settings:
        name = "chatbots_database"

    def get_context(self) -> str:
        context = f"""
            Summary of conversation: {', '.join(self.messages)}
            User profile:
            Username: {self.owner.username}
        """
        return context

    def generate_qa_template(self, question: str) -> str:
        template = f"""
            {self.purpose}/n
            {self.description}/n
            {self.prescription}/n
            {self.get_context()}/n
            User Query: {question}/n
            {self.name}AI Advice:
        """
        return template
    

class Message(Document):
    user: User
    username: str
    text: str
    chat: Chat
    type: str = Field(max_length=200)
    created_at: datetime.date = datetime.datetime.now()

    class Settings:
        name = "messages_database"
