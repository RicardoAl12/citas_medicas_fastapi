from fastapi import APIRouter, HTTPException
from models.cita import Cita
from repositories.cita_repo import CitaRepo

router = APIRouter(prefix="/citas", tags=["Citas"])

@router.post("/", response_model=Cita)
def crear_cita(cita: Cita):
    return CitaRepo.crear(cita)

@router.get("/", response_model=list[Cita])
def listar_citas():
    return CitaRepo.listar()

@router.get("/{cita_id}", response_model=Cita)
def obtener_cita(cita_id: int):
    cita = CitaRepo.obtener(cita_id)
    if not cita:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita

@router.put("/{cita_id}/estado")
def actualizar_estado(cita_id: int, estado: str):
    cita = CitaRepo.actualizar_estado(cita_id, estado)
    if not cita:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita

@router.delete("/{cita_id}")
def eliminar_cita(cita_id: int):
    if not CitaRepo.eliminar(cita_id):
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return {"ok": True}

@router.get("/medico/{medico_id}", response_model=list[Cita])
def citas_por_medico(medico_id: int):
    return CitaRepo.listar_por_medico(medico_id)

@router.get("/paciente/{paciente_id}", response_model=list[Cita])
def citas_por_paciente(paciente_id: int):
    return CitaRepo.listar_por_paciente(paciente_id)
