from fastapi import FastAPI
from app.api import users

app = FastAPI(title="Auth Service")

app.include_router(users.router, prefix="/auth", tags=["auth"])

@app.get("/health")
def health_check():
    return {"status": "ok"}