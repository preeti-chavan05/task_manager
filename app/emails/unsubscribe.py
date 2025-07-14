from fastapi import APIRouter

unsubscribe_router = APIRouter(prefix="/unsubscribe", tags=["unsubscribe"])

@unsubscribe_router.get("/")
def unsubscribe(email: str):
    return {"message": f"{email} has been unsubscribed from notifications."}