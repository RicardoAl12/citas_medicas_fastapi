from fastapi import APIRouter, HTTPException
from models.medico import Medico
from repositories.medico_repo import MedicoRepo

router = APIRouter(prefix="/medicos", tags=["Medicos"])

@router.post("/", response_model=Medico)
def crear_medico(medico: Medico):
    return MedicoRepo.crear(medico)

@router.get("/", response_model=list[Medico])
def listar_medicos():
    return MedicoRepo.listar()

@router.get("/{medico_id}", response_model=Medico)
def obtener_medico(medico_id: int):
    medico = MedicoRepo.obtener(medico_id)
    if not medico:
        raise HTTPException(status_code=404, detail="Médico no encontrado")
    return medico

@router.put("/{medico_id}", response_model=Medico)
def actualizar_medico(medico_id: int, medico: Medico):
    actualizado = MedicoRepo.actualizar(medico_id, medico)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Médico no encontrado")
    return actualizado

@router.delete("/{medico_id}")
def eliminar_medico(medico_id: int):
    if not MedicoRepo.eliminar(medico_id):
        raise HTTPException(status_code=404, detail="Médico no encontrado")
    return {"ok": True}
