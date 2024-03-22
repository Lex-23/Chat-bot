import beanie
import motor
import motor.motor_asyncio
import dotenv
import os
from models import User

dotenv.load_dotenv()

async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGO_DB_URL"))

    await beanie.init_beanie(
        database=client.db_name,
        document_models=[User]
    )