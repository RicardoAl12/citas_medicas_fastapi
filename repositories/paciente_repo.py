from models.paciente import Paciente

class PacienteRepo:
    _db = []
    _counter = 1

    @classmethod
    def listar(cls):
        return cls._db

    @classmethod
    def crear(cls, paciente: Paciente):
        paciente.id = cls._counter
        cls._counter += 1
        cls._db.append(paciente)
        return paciente

    @classmethod
    def obtener(cls, paciente_id: int):
        return next((p for p in cls._db if p.id == paciente_id), None)

    @classmethod
    def actualizar(cls, paciente_id: int, paciente: Paciente):
        obj = cls.obtener(paciente_id)
        if obj:
            obj.nombre = paciente.nombre
            obj.cedula = paciente.cedula
            obj.email = paciente.email
            obj.telefono = paciente.telefono
            return obj
        return None

    @classmethod
    def eliminar(cls, paciente_id: int):
        obj = cls.obtener(paciente_id)
        if obj:
            cls._db.remove(obj)
            return True
        return False
