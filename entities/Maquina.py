from .Requerimiento import Requerimiento

class Maquina:
    def __init__(self, code, descripcion, requerimientos: Requerimiento):
        self.code = code
        self.descripcion = descripcion
        self.requerimientos = requerimientos