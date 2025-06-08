class Maquina:
    def __init__(self, code: int, descripcion, requerimientos):
        self.code = code
        self.descripcion = descripcion
        self.requerimientos = requerimientos

    def costo_produccion(self):
        costo_total = 0
        for requerimiento in self.requerimientos:
            costo_total += requerimiento.pieza.costo * requerimiento.cantidad
        return costo_total
    
    def disponbilidad(self):
        pass

    def agregar_requerimiento(self):
        pass