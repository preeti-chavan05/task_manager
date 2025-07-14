from fastapi import APIRouter

tasks_router = APIRouter(prefix="/tasks", tags=["tasks"])

@tasks_router.get("/")
def get_tasks():
    return ["List of tasks"]