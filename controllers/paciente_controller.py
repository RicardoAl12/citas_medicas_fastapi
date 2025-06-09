from fastapi import APIRouter, HTTPException
from models.paciente import Paciente
from repositories.paciente_repo import PacienteRepo

router = APIRouter(prefix="/pacientes", tags=["Pacientes"])

@router.post("/", response_model=Paciente)
def crear_paciente(paciente: Paciente):
    return PacienteRepo.crear(paciente)

@router.get("/", response_model=list[Paciente])
def listar_pacientes():
    return PacienteRepo.listar()

@router.get("/{paciente_id}", response_model=Paciente)
def obtener_paciente(paciente_id: int):
    paciente = PacienteRepo.obtener(paciente_id)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente

@router.put("/{paciente_id}", response_model=Paciente)
def actualizar_paciente(paciente_id: int, paciente: Paciente):
    actualizado = PacienteRepo.actualizar(paciente_id, paciente)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return actualizado

@router.delete("/{paciente_id}")
def eliminar_paciente(paciente_id: int):
    if not PacienteRepo.eliminar(paciente_id):
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return {"ok": True}
