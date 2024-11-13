"""
Configuração da conexão com o banco de dados SQLite.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

DATABASE_URL = "sqlite:////app/data/orchestrateops.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """
    Inicializa o banco de dados, criando as tabelas.
    """
    Base.metadata.create_all(bind=engine)
