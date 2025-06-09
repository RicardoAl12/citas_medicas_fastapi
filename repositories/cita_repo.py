from models.cita import Cita

class CitaRepo:
    _db = []
    _counter = 1

    @classmethod
    def listar(cls):
        return cls._db

    @classmethod
    def crear(cls, cita: Cita):
        cita.id = cls._counter
        cls._counter += 1
        cls._db.append(cita)
        return cita

    @classmethod
    def obtener(cls, cita_id: int):
        return next((c for c in cls._db if c.id == cita_id), None)

    @classmethod
    def actualizar_estado(cls, cita_id: int, estado: str):
        cita = cls.obtener(cita_id)
        if cita:
            cita.estado = estado
            return cita
        return None

    @classmethod
    def eliminar(cls, cita_id: int):
        obj = cls.obtener(cita_id)
        if obj:
            cls._db.remove(obj)
            return True
        return False

    @classmethod
    def listar_por_medico(cls, medico_id: int):
        return [c for c in cls._db if c.medico_id == medico_id]

    @classmethod
    def listar_por_paciente(cls, paciente_id: int):
        return [c for c in cls._db if c.paciente_id == paciente_id]
