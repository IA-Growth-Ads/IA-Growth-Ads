from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# 🔹 Charger les variables d'environnement
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")

# 🔹 Configurer la connexion à la base de données PostgreSQL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
