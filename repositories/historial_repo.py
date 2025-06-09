from models.historial import Historial

class HistorialRepo:
    _db = []
    _counter = 1

    @classmethod
    def listar(cls):
        return cls._db

    @classmethod
    def crear(cls, historial: Historial):
        historial.id = cls._counter
        cls._counter += 1
        cls._db.append(historial)
        return historial

    @classmethod
    def listar_por_paciente(cls, paciente_id: int):
        return [h for h in cls._db if h.paciente_id == paciente_id]
