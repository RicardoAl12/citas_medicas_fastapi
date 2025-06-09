from fastapi import FastAPI
from controllers import paciente_controller, medico_controller, cita_controller, historial_controller

app = FastAPI(
    title="API de Gestión de Citas Médicas",
    description="Backend para el sistema de citas médicas (T02_03)",
    version="1.0"
)

app.include_router(paciente_controller.router)
app.include_router(medico_controller.router)
app.include_router(cita_controller.router)
app.include_router(historial_controller.router)
