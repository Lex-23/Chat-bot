from fastapi import APIRouter

from .users import router as user_router
from .profiles import router as profile_router

router = APIRouter()

router.include_router(user_router, tags=["Users"])
router.include_router(profile_router, tags=["Profiles"])
