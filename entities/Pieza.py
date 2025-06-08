class Pieza:
    def __init__(self, code: int, descripcion: str, costo: float, lote: int, cantidad: int):
        self.code = code
        self.descripcion = descripcion
        self.costo = costo
        self.lote = lote
        self.cantidad = cantidad