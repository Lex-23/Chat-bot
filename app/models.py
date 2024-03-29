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
    owner: BackLink[User] = Field(original_field="chats")
    messages: Optional[Union[List[Link[Message]], None]]
    created_at: datetime.date = datetime.datetime.now()
    updated_at: datetime.date = datetime.datetime.now()
    is_active: bool = True
    type: str
    last_message: Optional[Union[Link[Message], None]]


class ChatBot(Chat):
    purpose: str
    description: str = Field(max_length=1000)
    prescription: str = Field(max_length=1000)
    communicative_style: str = Field(max_length=500)

    class Settings:
        name = "chatbots_database"

    def generate_conversation_summary(self, limit: int = 10):
        messages = self.messages[-limit:]
        signed_messages = [f"{msg.username} said: {msg}" for msg in messages]
        return ', '.join(signed_messages)

    def get_context(self) -> str:
        profile = Profile.get(user = self.owner)
        context = f"""
            Summary of conversation: {', '.join(self.generate_conversation_summary())}
            User profile:
            Username: {self.owner.ref.username}
            Email: {profile.email}
            Age: {profile.age} 
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
    user: Link[User]
    username: str
    text: str
    chat: BackLink[Chat] = Field(original_field="messages")
    type: str = Field(max_length=200)
    created_at: datetime.date = datetime.datetime.now()

    class Settings:
        name = "messages_database"
