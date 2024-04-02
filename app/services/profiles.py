from models import Profile, User
from typing import List
from beanie import PydanticObjectId


def list_profiles() -> List[Profile]:
    return Profile.find_all().to_list()

def get_profile(user: User) -> Profile:
    return Profile.find_one({"username": user.username})

def create_profile(profile: Profile) -> None:
    return profile.create()

def update_profile(profile: Profile, data: dict) -> Profile:
    for attr in data:
        if hasattr(profile, attr):
            setattr(profile, attr, data[attr])
    return profile.save()

def delete_profile(profile: Profile) -> None:
    return profile.delete()
