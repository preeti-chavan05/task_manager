from fastapi import FastAPI
from app.database import Base, engine
from app.auth.routes import auth_router
from app.users.routes import users_router
from app.tasks.routes import tasks_router
from app.emails.unsubscribe import unsubscribe_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(tasks_router)
app.include_router(unsubscribe_router)

@app.get("/")
def root():
    return {"message": "Task Manager API is running"}