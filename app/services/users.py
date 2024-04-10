from models import User
from typing import List
from beanie import PydanticObjectId
import pdb


def list_users() -> List[User]:
    # pdb.set_trace()
    # users = await User.find_all().to_list()
    # pdb.set_trace()
    # return users
    return User.find_all().to_list()

def get_user(user_id: PydanticObjectId) -> User:
    return User.get(user_id)

def create_user(user: User) -> None:
    return user.create()

def update_user(user: User, data: dict) -> User:
    for attr in data:
        if hasattr(user, attr):
            setattr(user, attr, data[attr])
    return user.save()

def delete_user(user: User) -> None:
    return user.delete()

def is_user_exists(username: str) -> bool:
    return User.find_one(User.username == username).exists()
