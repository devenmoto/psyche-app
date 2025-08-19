from app.domain.user import User
from app.infrastructure.db.session import SessionLocal
from app.infrastructure.db.models import UserModel

class UserRepository:
    def save(self, user: User):
        db = SessionLocal()
        db_user = UserModel(username=user.username, email=user.email, hashed_password=user.hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user