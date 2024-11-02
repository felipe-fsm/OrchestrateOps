"""
Ponto de entrada da aplicação OrchestrateOps.
"""
from fastapi import FastAPI
from app.api import requests
from app.database import init_db

app = FastAPI(
    title="OrchestrateOps API",
    description="API para controle de solicitações de compra.",
    version="1.0.0"
)

# Inicializa o banco de dados ao iniciar
@app.on_event("startup")
def startup_event():
    init_db()

# Inclui as rotas definidas no módulo requests
app.include_router(requests.router)
