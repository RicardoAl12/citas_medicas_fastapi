from models.cita import Cita
from repositories.cita_repo import CitaRepo
from datetime import datetime

def setup_function():
    CitaRepo._db.clear()
    CitaRepo._counter = 1

def test_crear_cita():
    cita = Cita(paciente_id=1, medico_id=1, fecha_hora=datetime.now(), motivo="Chequeo")
    creada = CitaRepo.crear(cita)
    assert creada.id == 1
    assert creada.motivo == "Chequeo"
    assert creada.estado == "Pendiente"

def test_listar_citas():
    CitaRepo.crear(Cita(paciente_id=1, medico_id=1, fecha_hora=datetime.now(), motivo="Uno"))
    CitaRepo.crear(Cita(paciente_id=2, medico_id=2, fecha_hora=datetime.now(), motivo="Dos"))
    lista = CitaRepo.listar()
    assert len(lista) == 2

def test_actualizar_estado():
    cita = CitaRepo.crear(Cita(paciente_id=1, medico_id=1, fecha_hora=datetime.now(), motivo="Motivo"))
    actualizada = CitaRepo.actualizar_estado(cita.id, "Confirmada")
    assert actualizada.estado == "Confirmada"

def test_eliminar_cita():
    cita = CitaRepo.crear(Cita(paciente_id=1, medico_id=1, fecha_hora=datetime.now(), motivo="Motivo"))
    res = CitaRepo.eliminar(cita.id)
    assert res is True
    assert CitaRepo.obtener(cita.id) is None
