from models.historial import Historial
from repositories.historial_repo import HistorialRepo

def setup_function():
    HistorialRepo._db.clear()
    HistorialRepo._counter = 1

def test_crear_historial():
    historial = Historial(paciente_id=1, descripcion="Diagnóstico X", fecha="2024-06-10", medico_id=1)
    creado = HistorialRepo.crear(historial)
    assert creado.id == 1
    assert creado.descripcion == "Diagnóstico X"

def test_listar_historiales():
    HistorialRepo.crear(Historial(paciente_id=1, descripcion="Uno", fecha="2024-01-01", medico_id=1))
    HistorialRepo.crear(Historial(paciente_id=2, descripcion="Dos", fecha="2024-01-01", medico_id=2))
    lista = HistorialRepo.listar()
    assert len(lista) == 2

def test_listar_por_paciente():
    HistorialRepo.crear(Historial(paciente_id=1, descripcion="A", fecha="2024-01-01", medico_id=1))
    HistorialRepo.crear(Historial(paciente_id=2, descripcion="B", fecha="2024-01-01", medico_id=2))
    por_paciente = HistorialRepo.listar_por_paciente(1)
    assert len(por_paciente) == 1
    assert por_paciente[0].descripcion == "A"
