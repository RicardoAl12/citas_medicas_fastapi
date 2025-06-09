from pydantic import BaseModel

class Paciente(BaseModel):
    id: int | None = None
    nombre: str
    cedula: str
    email: str
    telefono: str
