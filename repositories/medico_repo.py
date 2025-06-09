from models.medico import Medico

class MedicoRepo:
    _db = []
    _counter = 1

    @classmethod
    def listar(cls):
        return cls._db

    @classmethod
    def crear(cls, medico: Medico):
        medico.id = cls._counter
        cls._counter += 1
        cls._db.append(medico)
        return medico

    @classmethod
    def obtener(cls, medico_id: int):
        return next((m for m in cls._db if m.id == medico_id), None)

    @classmethod
    def actualizar(cls, medico_id: int, medico: Medico):
        obj = cls.obtener(medico_id)
        if obj:
            obj.nombre = medico.nombre
            obj.especialidad = medico.especialidad
            obj.email = medico.email
            obj.telefono = medico.telefono
            return obj
        return None

    @classmethod
    def eliminar(cls, medico_id: int):
        obj = cls.obtener(medico_id)
        if obj:
            cls._db.remove(obj)
            return True
        return False
