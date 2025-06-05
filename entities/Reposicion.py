class Reposicion:
    def __init__(self, pieza, cantidad_lotes, fecha_reposicion):
        self.pieza = pieza
        self.cantidad_lotes = cantidad_lotes
        self.fecha_reposicion = fecha_reposicion
        
    def costo_reposicion(self):
        return self.cantidad_lotes * self.pieza.lote * self.pieza.costo