"""
Define as operações CRUD para o modelo de Solicitação de Compra.
"""
from sqlalchemy.orm import Session
from app import schemas
from .models import SolicitacaoCompra


def criar_solicitacao(db: Session, solicitacao: schemas.SolicitacaoCreate):
    """
    Adiciona uma nova solicitação de compra ao banco de dados.
    """
    # Converte o schema Pydantic para o modelo ORM
    db_solicitacao = SolicitacaoCompra(
        setor=solicitacao.setor,
        solicitante=solicitacao.solicitante,
        produto=solicitacao.produto,
        quantidade=solicitacao.quantidade,
        status=solicitacao.status
    )
    db.add(db_solicitacao)
    db.commit()
    db.refresh(db_solicitacao)
    return db_solicitacao


def listar_solicitacoes(db: Session):
    """
    Lista todas as solicitações de compra.
    """
    return db.query(SolicitacaoCompra).all()


def obter_solicitacao_por_id(db: Session, solicitacao_id: int):
    """
    Obtém uma solicitação de compra pelo ID.
    """
    return db.query(SolicitacaoCompra).filter(SolicitacaoCompra.id == solicitacao_id).first()


def atualizar_status(db: Session, solicitacao_id: int, novo_status: str):
    """
    Atualiza o status de uma solicitação de compra.

    Parâmetros:
    - db: Sessão do banco de dados.
    - solicitacao_id: ID da solicitação a ser atualizada.
    - novo_status: Novo status para a solicitação.
    """
    solicitacao = db.query(SolicitacaoCompra).filter(SolicitacaoCompra.id == solicitacao_id).first()
    if solicitacao:
        solicitacao.status = novo_status
        db.commit()
        db.refresh(solicitacao)
    return solicitacao


def deletar_solicitacao(db: Session, solicitacao_id: int):
    """
    Deleta uma solicitação de compra.

    Parâmetros:
    - db: Sessão do banco de dados.
    - solicitacao_id: ID da solicitação a ser deletada.
    """
    solicitacao = db.query(SolicitacaoCompra).filter(SolicitacaoCompra.id == solicitacao_id).first()
    if solicitacao:
        db.delete(solicitacao)
        db.commit()
    return solicitacao
