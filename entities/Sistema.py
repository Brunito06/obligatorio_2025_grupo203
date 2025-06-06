import datetime

#Exceptions
from exceptions import ExceptionClienteYaExiste

#Entities
from entities import Cliente 
from entities.Pieza import Pieza
from entities.Maquina import Maquina
from entities.Requerimiento import Requerimiento
from entities.Reposicion import Reposicion
from entities.Pedido import Pedido

class Sistema():
    def __init__(self):
        self.__clientes = []
        self.__piezas = []
        self.__maquinas = []
        self.__pedidos = []
    
    @property
    def clientes(self):
        return self.__clientes

    @clientes.setter
    def clientes(self, value):
        self.__clientes = value

    @property
    def piezas(self):
        return self.__piezas

    @property
    def maquinas(self):
        return self.__maquinas
    
    @property
    def pedidos(self):
        return self.__pedidos


##########CLIENTES##########
    def generar_id_cliente(self):
        return len(self.clientes) + 1 

    def registrar_cliente_particular(self, telefono, email, dni, nombre):
        id = self.generar_id_cliente()
        nuevo = Cliente.ClienteParticular(id, telefono, email, dni, nombre)
        self.clientes.append(nuevo)

        print(f"Cliente registrado con ID: {nuevo.id}")

        return nuevo

    def registrar_cliente_empresa(self, telefono, email, rut, nombre, web):
        id = self.generar_id_cliente()
        nuevo = Cliente.ClienteEmpresa(id, telefono, email, rut, nombre, web)
        self.clientes.append(nuevo)
        return nuevo

    def listar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados - Volviendo al menú principal")
            return
        for cliente in self.clientes:
            if cliente.tipo_cliente == "Empresa":
                print(f"ID: {cliente.id} | Tipo: Empresa | Nombre: {cliente.nombre} | RUT: {cliente.rut} | Teléfono: {cliente.telefono} | Email: {cliente.email} | Web: {cliente.web}")
            else:
                print(f"ID: {cliente.id} | Tipo: Particular | Nombre: {cliente.nombre} | DNI: {cliente.dni} | Teléfono: {cliente.telefono} | Email: {cliente.email}")

##########PIEZAS##########
    def generar_code_pieza(self):
        return len(self.piezas) + 1 
    
    def registrar_pieza(self, descripcion, costo, lote, cantidad):
        code = self.generar_code_pieza()
        pieza_nueva = Pieza(code, descripcion, costo, lote, cantidad)
        self.piezas.append(pieza_nueva)
        return pieza_nueva

    def listar_piezas(self):
        if not self.piezas:
            print("No hay piezas registradas - Volviendo al menú principal")
            return
        for pieza in self.piezas:
            print(f"Código: {pieza.code} | Descripción: {pieza.descripcion} | Costo: {pieza.costo} | Lote: {pieza.lote} | Cantidad: {pieza.cantidad}")

##########MAQUINA##########
    def generar_code_maquina(self):
        return len(self.maquinas) + 1
    
    def registrar_maquina(self, descripcion, requerimientos):
        code = self.generar_code_maquina()
        maquina_nueva = Maquina(code, descripcion, requerimientos)
        self.maquinas.append(maquina_nueva)
        return maquina_nueva

    def listar_maquinas(self):
        if not self.maquinas:
            print("No hay máquinas registradas - Volviendo al menú principal")
            return
        
        for maquina in self.maquinas:
            lista_requerimientos = ""
            for requerimiento in maquina.requerimientos:
                lista_requerimientos += f"\n * {requerimiento}"
            print(f"Código: {maquina.code} | Descripción: {maquina.descripcion} | Costo de produccion: {maquina.costo_produccion()} \nRequerimientos: {lista_requerimientos}\n")

##########REQUERIMIENTO##########
    def registrar_requerimiento(self, maquina, pieza, cantidad):
        nuevo_requerimiento = Requerimiento(maquina, pieza, cantidad)
        return nuevo_requerimiento
    
    def actualizar_pedidos(self):
        for pedido in self.pedidos:
            if pedido.estado == "Pendiente":
                requerimientos_completos = 0
                for requerimiento in pedido.maquina.requerimientos:
                    for pieza in self.piezas:
                        if requerimiento.pieza.code == pieza.code:
                            if requerimiento.cantidad <= pieza.cantidad:
                                requerimientos_completos += 1
                
                if requerimientos_completos == len(pedido.maquina.requerimientos):
                    pedido.estado = "Entregado"
                    pedido.fecha_entregado = datetime.datetime.now()

                    for pieza in self.piezas:
                        for requerimiento in pedido.maquina.requerimientos:
                            if requerimiento.pieza.code == pieza.code:
                                pieza.cantidad -= requerimiento.cantidad

##########REPOSICION##########
    def generar_reposicion(self, pieza, cantidad_lotes, fecha_reposicion):
        reposicion_nueva = Reposicion(pieza, cantidad_lotes, fecha_reposicion)
        pieza.cantidad += cantidad_lotes * pieza.lote
        costo_reposicion = reposicion_nueva.costo_reposicion()
        self.actualizar_pedidos()
        return costo_reposicion
    
##########PEDIDO##########

    def registrar_pedido(self, cliente, maquina, fecha_recibido, fecha_entregado, estado):
        nuevo_pedido = Pedido(cliente, maquina, fecha_recibido, fecha_entregado, estado)
        self.pedidos.append(nuevo_pedido)
        self.actualizar_pedidos()
        return nuevo_pedido
    
    def listar_pedidos(self):
        if not self.pedidos:
            print("No hay pedidos registrados - Volviendo al menú principal")
            return
        
        for pedido in self.pedidos:
            print(f"Cliente: {pedido.cliente.nombre} | Máquina: {pedido.maquina.descripcion} | Fecha Recibido: {pedido.fecha_recibido} | Fecha Entregado: {pedido.fecha_entregado} | Estado: {pedido.estado}")