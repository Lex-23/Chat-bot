from models import Profile, User, ChatBot, Message
from typing import List
from beanie import PydanticObjectId


def list_chatbots() -> List[ChatBot]:
    return ChatBot.find_all().to_list()

def get_chatbot(bot_id: PydanticObjectId) -> ChatBot:
    return ChatBot.get(bot_id)

def create_chatbot(bot: ChatBot) -> None:
    return bot.create()

def update_chatbot(bot: ChatBot, data: dict) -> ChatBot:
    for attr in data:
        if hasattr(bot, attr):
            setattr(bot, attr, data[attr])
    return bot.save()

def delete_chatbot(bot: ChatBot) -> None:
    return bot.delete()

def text_to_bot(bot: ChatBot, msg: Message) -> Message:
    pass
