from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@db:5432/psique"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)