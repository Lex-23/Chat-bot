from __future__ import annotations
from beanie import Document, Link, BackLink
import datetime
from pydantic import Field
from typing import Optional, Union, List


class User(Document):
    username: str = Field(max_length=100)
    created_at: datetime.date = datetime.date.today()
    chats: Optional[Union[List[Link[Chat]], None]] = None

    class Settings:
        name = "users_database"

    class Config:
        json_schema_extra = {
            "username": "John",
            "created_at": datetime.date.today(),
            "is_active": True,
            "chats": []
        }

class Profile(Document):
    user: Link[User]
    username: str
    email: str
    age: int
    bio: Optional[Union[str, None]] = Field(max_length=1000)

    class Settings:
        name = "profiles_database"



class Chat(Document):
    name: str = Field(max_length=200)
    type: str = Field(max_length=200)
    owner_username: str = Field(max_length=100)
    owner: Link[User] = Field()
    messages: Optional[List[Message]] = []
    created_at: datetime.date = datetime.date.today()
    updated_at: datetime.date = datetime.date.today()
    is_active: bool = True
    last_message: Optional[Message] = None


class ChatBot(Chat):
    description: str = Field(max_length=1000)
    prescription: str = Field(max_length=1000)
    communicative_style: str = Field(max_length=500)

    class Settings:
        name = "chatbots_database"

    def generate_conversation_summary(self, limit: int = 20):
        messages = self.messages[-limit:]
        signed_messages = [f"{msg.username.title()} said: {msg.text}." for msg in messages]
        return ', '.join(signed_messages)

    async def get_context(self) -> str:
        profile = await Profile.find_one({"username": self.owner_username})
        context = f"""
            Summary of the conversation: {self.generate_conversation_summary() if self.messages else ""}
            User profile:
            Username: {self.owner_username}
            Email: {profile.email}
            Age: {profile.age}
        """
        return context

    def generate_qa_template(self, question: str) -> str:

        template = f"""
            {self.description}/n
            {self.prescription}/n
            {self.communicative_style}/n
            User Query: {question}/n
            {self.name} Advice:
        """
        return template
    

class Message(Document):
    user: Link[User]
    username: str
    text: str
    chat: Link[ChatBot]
    type: str = Field(max_length=200)
    created_at: datetime.datetime = datetime.datetime.now()

    class Settings:
        name = "messages_database"
