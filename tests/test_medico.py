from models.medico import Medico
from repositories.medico_repo import MedicoRepo

def setup_function():
    MedicoRepo._db.clear()
    MedicoRepo._counter = 1

def test_crear_medico():
    medico = Medico(nombre="Dra. Ana", especialidad="Cardiología", email="ana@medico.com", telefono="0999111222")
    creado = MedicoRepo.crear(medico)
    assert creado.id == 1
    assert creado.especialidad == "Cardiología"

def test_listar_medicos():
    MedicoRepo.crear(Medico(nombre="Ana", especialidad="Cardio", email="a@a.com", telefono="1"))
    MedicoRepo.crear(Medico(nombre="Luis", especialidad="Pediatra", email="b@b.com", telefono="2"))
    lista = MedicoRepo.listar()
    assert len(lista) == 2

def test_actualizar_medico():
    creado = MedicoRepo.crear(Medico(nombre="Original", especialidad="General", email="a@a.com", telefono="1"))
    actualizado = Medico(nombre="Nuevo", especialidad="Dermatología", email="nuevo@medico.com", telefono="3")
    MedicoRepo.actualizar(creado.id, actualizado)
    m = MedicoRepo.obtener(creado.id)
    assert m.nombre == "Nuevo"
    assert m.especialidad == "Dermatología"

def test_eliminar_medico():
    creado = MedicoRepo.crear(Medico(nombre="Ana", especialidad="Cardio", email="a@a.com", telefono="1"))
    res = MedicoRepo.eliminar(creado.id)
    assert res is True
    assert MedicoRepo.obtener(creado.id) is None
