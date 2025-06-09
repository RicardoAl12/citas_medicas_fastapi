from pydantic import BaseModel

class Historial(BaseModel):
    id: int | None = None
    paciente_id: int
    descripcion: str
    fecha: str
    medico_id: int
