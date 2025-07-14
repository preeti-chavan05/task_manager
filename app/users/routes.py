from fastapi import APIRouter

users_router = APIRouter(prefix="/users", tags=["users"])

@users_router.get("/me")
def get_my_profile():
    return {"message": "User profile info"}