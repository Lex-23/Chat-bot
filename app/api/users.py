from fastapi import APIRouter, HTTPException, Request
from models import User
from typing import List
from beanie import PydanticObjectId
from services import get_user, list_users, create_user, update_user, delete_user, is_user_exists


router = APIRouter()

@router.get("/users/me")
async def read_current_user(request: Request):
    return {"username": request.user.username}

@router.get('/users', status_code=200)
async def list() -> List[User]:
    return await list_users()

    
@router.post('/users', status_code=201)
async def create(user: User) -> dict:
    if not await is_user_exists(user.username):
        await create_user(user)
        return {"message": f"User <{user.username}> has been saved"}
    else:
        raise HTTPException(status_code=400, detail=f"User with username <{user.username}> already exists")
 

@router.get('/users/{user_id}', status_code=200)
async def retreive(user_id: PydanticObjectId) -> User:
    user = await get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put('/users/{user_id}', status_code=200)
async def update(user_id: PydanticObjectId, data: dict) -> User:
    user_to_update = await get_user(user_id)
    if not user_to_update:
        raise HTTPException(status_code=404, detail="Resource has not found")
    return await update_user(user=user_to_update, data=data)


@router.delete('/users/{user_id}', status_code=204)
async def delete(user_id: PydanticObjectId) -> None:
    user_to_delete = await get_user(user_id)
    if not user_to_delete:
        raise HTTPException(status_code=404, detail="Resource has not found")
    await delete_user(user_to_delete)
