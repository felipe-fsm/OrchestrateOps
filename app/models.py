"""
Define o modelo de dados para as solicitações de compra.
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SolicitacaoCompra(Base):
    """
    Modelo de dados para uma solicitação de compra.
    """
    __tablename__ = "solicitacoes_compras"
    
    id = Column(Integer, primary_key=True, index=True)
    setor = Column(String, index=True)
    solicitante = Column(String)
    produto = Column(String)
    quantidade = Column(Integer)
    status = Column(String, default="pendente")
