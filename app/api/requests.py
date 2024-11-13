"""
Define as rotas da API para as solicitações de compra.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud_operations, schemas, database

router = APIRouter()

def get_db():
    """
    Retorna uma sessão de conexão com o banco de dados.
    """
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/solicitacoes/", response_model=schemas.Solicitacao)
def criar_solicitacao(solicitacao: schemas.SolicitacaoCreate, db: Session = Depends(get_db)):
    """
    Cria uma nova solicitação de compra.
    """
    return crud_operations.criar_solicitacao(db=db, solicitacao=solicitacao)

@router.get("/solicitacoes/", response_model=list[schemas.Solicitacao])
def listar_solicitacoes(db: Session = Depends(get_db)):
    """
    Lista todas as solicitações de compra.
    """
    return crud_operations.listar_solicitacoes(db=db)

@router.get("/solicitacoes/{solicitacao_id}", response_model=schemas.Solicitacao)
def obter_solicitacao(solicitacao_id: int, db: Session = Depends(get_db)):
    """
    Obtém uma solicitação de compra pelo ID.
    """
    solicitacao = crud_operations.obter_solicitacao_por_id(db, solicitacao_id)
    if solicitacao is None:
        raise HTTPException(status_code=404, detail="Solicitação não encontrada")
    return solicitacao

@router.put("/solicitacoes/{solicitacao_id}", response_model=schemas.Solicitacao)
def atualizar_status(solicitacao_id: int, status_update: schemas.StatusUpdate, db: Session = Depends(get_db)):
    """
    Atualiza o status de uma solicitação de compra.
    """
    solicitacao = crud_operations.atualizar_status(db, solicitacao_id, status_update.status)
    if solicitacao is None:
        raise HTTPException(status_code=404, detail="Solicitação não encontrada")
    return solicitacao

@router.delete("/solicitacoes/{solicitacao_id}", response_model=schemas.Solicitacao)
def deletar_solicitacao(solicitacao_id: int, db: Session = Depends(get_db)):
    """
    Deleta uma solicitação de compra.
    """
    solicitacao = crud_operations.deletar_solicitacao(db, solicitacao_id)
    if solicitacao is None:
        raise HTTPException(status_code=404, detail="Solicitação não encontrada")
    return solicitacao
