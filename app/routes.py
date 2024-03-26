from fastapi import APIRouter, HTTPException
from models import User
from typing import List
from beanie import PydanticObjectId

router = APIRouter()

@router.get('/users', status_code=200)
async def list_users() -> List[User]:
    users = await User.find_all().to_list()
    return users


@router.post('/users', status_code=201)
async def create_user(user: User) -> dict:
    await user.create()

    return {"message": "User has been saved"} 

@router.get('/users/{user_id}', status_code=200)
async def retreive_user(user_id: PydanticObjectId) -> User:
    user = await User.get(user_id)

    return user

@router.put('/users/{user_id}', status_code=200)
async def update_user(user: User, user_id: PydanticObjectId) -> User:
    user_to_update = await User.get(user_id)
    if not user_to_update:
        raise HTTPException(
            status_code=404,
            detail="Resource has not found"
        )
    user_to_update.username = user.username
    user_to_update.chats = user.chats
    await user_to_update.save()

    return user_to_update

@router.delete('/users/{user_id}', status_code=204)
async def delete_user(user_id: PydanticObjectId):
    user_to_delete = await User.get(user_id)
    if not user_to_delete:
        raise HTTPException(
            status_code=404,
            detail="Resource has not found"
        )
    await user_to_delete.delete()

    return {"message": f"User {user_to_delete.username} was deleted"}
