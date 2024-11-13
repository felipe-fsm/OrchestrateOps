"""
Define os schemas para validação e serialização das solicitações de compra.
"""
from pydantic import BaseModel

class SolicitacaoBase(BaseModel):
    """
    Schema base para criação de uma solicitação de compra.
    """
    setor: str
    solicitante: str
    produto: str
    quantidade: int
    status: str = "pendente"

class SolicitacaoCreate(SolicitacaoBase):
    """
    Schema para criação de uma nova solicitação de compra.
    """
    pass

class Solicitacao(SolicitacaoBase):
    """
    Schema completo de uma solicitação de compra, incluindo o ID.
    """
    id: int

    class Config:
        orm_mode = True

class StatusUpdate(BaseModel):
    """
    Schema para atualização do status de uma solicitação de compra.
    """
    status: str

