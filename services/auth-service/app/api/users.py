from fastapi import APIRouter, Depends
from app.application.use_cases.register_user import RegisterUser
from app.infrastructure.repositories.user_repository import UserRepository

router = APIRouter()

@router.post("/register")
def register_user(username: str, email: str, password: str):
    repo = UserRepository()
    use_case = RegisterUser(repo)
    return use_case.execute(username, email, password)