from pydantic import BaseModel
from datetime import datetime

class Cita(BaseModel):
    id: int | None = None
    paciente_id: int
    medico_id: int
    fecha_hora: datetime
    motivo: str
    estado: str = "Pendiente"
