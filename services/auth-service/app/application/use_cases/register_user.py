from app.domain.user import User
from app.infrastructure.security.password_hasher import PasswordHasher

class RegisterUser:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, username: str, email: str, password: str):
        hashed = PasswordHasher.hash(password)
        user = User(id=None, username=username, email=email, hashed_password=hashed)
        return self.user_repository.save(user)