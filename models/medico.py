from pydantic import BaseModel

class Medico(BaseModel):
    id: int | None = None
    nombre: str
    especialidad: str
    email: str
    telefono: str
