from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Konekcijski string (URL) ka našoj Postgres bazi iz Docker-a
# Format: postgresql://user:password@host:port/dbname
SQLALCHEMY_DATABASE_URL = "postgresql://admin:password123@localhost:5432/document_db"

# Engine je "motor" koji uspostavlja fizičku konekciju sa bazom
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal je fabrika za kreiranje kratkotrajnih sesija (konekcija) za svaki API zahtev
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base je osnovna klasa koju će sve naše tabele nasleđivati
Base = declarative_base()