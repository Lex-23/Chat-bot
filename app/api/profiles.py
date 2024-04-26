from fastapi import APIRouter, HTTPException, Depends, Request, Body
from models import Profile
from typing import List, Annotated
from services import *


router = APIRouter()

@router.get('/profiles', status_code=200)
async def list() -> List[Profile]:
    return await list_profiles()

@router.post('/profiles', status_code=201)
async def create(
    request: Request, 
    data: Annotated[
        dict,
        Body(examples=[
            {
            "email": "user.email@mail.com",
            "age": 20,
            "bio": "A python developer with more than 4 years of experience.",
            },
        ])
    ]
    ) -> dict:
    data['user'] = request.user
    data['username'] = request.user.username
    profile = Profile(**data)
    await create_profile(profile)
    return {"message": f"Profile for user <{profile.user.username}> has been saved"}
 

@router.get('/profiles/me', status_code=200)
async def retreive(request: Request) -> Profile:
    profile = await get_profile(request.user)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile


@router.put('/profiles', status_code=200)
async def update(request: Request, data: dict) -> Profile:
    profile_to_update = await get_profile(request.user)
    if profile_to_update is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return await update_profile(profile=profile_to_update, data=data)

@router.delete('/profiles', status_code=204)
async def delete(request: Request):
    profile_to_delete = await get_profile(request.user)
    if profile_to_delete is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    await delete_profile(profile_to_delete)
