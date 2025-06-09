from fastapi import APIRouter
from models.historial import Historial
from repositories.historial_repo import HistorialRepo

router = APIRouter(prefix="/historiales", tags=["Historiales"])

@router.post("/", response_model=Historial)
def crear_historial(historial: Historial):
    return HistorialRepo.crear(historial)

@router.get("/", response_model=list[Historial])
def listar_historiales():
    return HistorialRepo.listar()

@router.get("/paciente/{paciente_id}", response_model=list[Historial])
def historiales_por_paciente(paciente_id: int):
    return HistorialRepo.listar_por_paciente(paciente_id)
