from models.paciente import Paciente
from repositories.paciente_repo import PacienteRepo

def setup_function():
    PacienteRepo._db.clear()
    PacienteRepo._counter = 1

def test_crear_paciente():
    paciente = Paciente(nombre="Juan Perez", cedula="0102030405", email="juan@mail.com", telefono="0999888777")
    creado = PacienteRepo.crear(paciente)
    assert creado.id == 1
    assert creado.nombre == "Juan Perez"

def test_listar_pacientes():
    PacienteRepo.crear(Paciente(nombre="Test1", cedula="1", email="a@a.com", telefono="1"))
    PacienteRepo.crear(Paciente(nombre="Test2", cedula="2", email="b@b.com", telefono="2"))
    lista = PacienteRepo.listar()
    assert len(lista) == 2

def test_actualizar_paciente():
    creado = PacienteRepo.crear(Paciente(nombre="Original", cedula="1", email="a@a.com", telefono="1"))
    actualizado = Paciente(nombre="Nuevo", cedula="2", email="b@b.com", telefono="2")
    PacienteRepo.actualizar(creado.id, actualizado)
    p = PacienteRepo.obtener(creado.id)
    assert p.nombre == "Nuevo"
    assert p.cedula == "2"

def test_eliminar_paciente():
    creado = PacienteRepo.crear(Paciente(nombre="Test", cedula="1", email="a@a.com", telefono="1"))
    res = PacienteRepo.eliminar(creado.id)
    assert res is True
    assert PacienteRepo.obtener(creado.id) is None
