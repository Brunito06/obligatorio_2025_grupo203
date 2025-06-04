class Requerimiento:
    def __init__(self, maquina, pieza, cantidad):
        self.maquina = maquina
        self.pieza = pieza
        self.cantidad = cantidad

    def __str__(self):
        return f"Descripcion:{self.pieza.descripcion}, Cantidad: {self.cantidad}"