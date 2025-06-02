from .Cliente import Cliente
from .Maquina import Maquina

class Pedido:
    def __init__(self, cliente: Cliente, maquina: Maquina, estado, fecha_recepcion, precio_final, fecha_entrega):
        self.cliente = cliente
        self.maquina = maquina
        self.estado = estado
        self.fecha_recepcion = fecha_recepcion
        self.fecha_entrega = fecha_entrega
        self.precio_final = precio_final
