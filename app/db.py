import beanie
import motor
import motor.motor_asyncio
import dotenv
from models import User, ChatBot, Message, Profile

config = dotenv.dotenv_values(".env")

MONGO_URL = config.get('MONGO_DB_URL')
DB_NAME = config.get('PROJECT_DB_NAME')

async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)

    await beanie.init_beanie(
        database=client[DB_NAME],
        document_models=[User, Profile, ChatBot, Message]
    )
