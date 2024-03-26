import beanie
import motor
import motor.motor_asyncio
import dotenv
import os
from models import User, ChatBot, Message

dotenv.load_dotenv()

MONGO_URL = os.getenv("MONGO_DB_URL")
DB_NAME = os.getenv('PROJECT_DB_NAME')

async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)

    await beanie.init_beanie(
        database=client[DB_NAME],
        document_models=[User, ChatBot, Message]
    )
