from fastapi import APIRouter, HTTPException, Depends, Request
from models import User
from typing import List
from beanie import PydanticObjectId


router = APIRouter()

@router.get("/users/me")
def read_current_user(request: Request):
    return {"username": request.user.username}

@router.get('/users', status_code=200)
async def list_users() -> List[User]:
    users = await User.find_all().to_list()
    return users


@router.post('/users', status_code=201)
async def create_user(user: User) -> dict:
    if not User.find_one(User.username == user.username):
        await user.create()
        return {"message": f"User <{user.username}> has been saved"}
    else:
        raise HTTPException(
            status_code=400,
            detail=f"User with username <{user.username}> already exists"
        )
 

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
    await user_to_update.set(
        {
            User.username: user.username,
            User.chats: user.chats
        }
    )
    
    updated_user = await user_to_update.sync()
    return updated_user

@router.delete('/users/{user_id}', status_code=204)
async def delete_user(user_id: PydanticObjectId):
    user_to_delete = await User.get(user_id)
    if not user_to_delete:
        raise HTTPException(
            status_code=404,
            detail="Resource has not found"
        )
    await user_to_delete.delete()

    return {"message": f"User <{user_to_delete.username}> was deleted succesfully"}
