from models import Profile, User, ChatBot, Message
from typing import List
from beanie import PydanticObjectId
from .ai_integration import send_message_to_ai


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

async def text_to_bot(user: User, bot: ChatBot, msg: str) -> str:
    user_message = Message(
        user=user,
        username=user.username,
        text=msg,
        chat=bot,
        type="Bot"
    )
    await user_message.save()
    bot.messages.append(user_message)
    bot.last_message = user_message
    await bot.save()
    response = await send_message_to_ai(chatbot=bot, question=msg)
    bot_message = Message(
        user=user,
        username=bot.name,
        text=response,
        chat=bot,
        type="Bot"
    )
    await bot_message.save()
    bot.messages.append(bot_message)
    bot.last_message = bot_message
    await bot.save()
    return response
