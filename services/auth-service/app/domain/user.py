from dataclasses import dataclass

@dataclass
class User:
    id: int | None
    username: str
    email: str
    hashed_password: str