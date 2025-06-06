import datetime

from .Cliente import Cliente
from .Maquina import Maquina

class Pedido:
    def __init__(self, cliente: Cliente, maquina: Maquina, fecha_recibido: datetime, fecha_entregado: datetime, estado: str):
        self.cliente = cliente
        self.maquina = maquina
        self.fecha_recibido = fecha_recibido
        self.fecha_entregado = fecha_entregado
        self.estado = estado