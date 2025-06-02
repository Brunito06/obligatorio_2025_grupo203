#Exceptions
from exceptions import ExceptionClienteYaExiste

#Entities
from entities import Cliente 
from entities.Pieza import Pieza
from entities.Maquina import Maquina

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


##########CLIENTES##########
    def generar_id_cliente(self):
        return len(self.clientes) + 1 

    def registrar_cliente_particular(self, telefono, email, dni, nombre):
        id = self.generar_id_cliente()
        nuevo = Cliente.ClienteParticular(id, telefono, email, dni, nombre)
        self.clientes.append(nuevo)

        print(f"Cliente registrado con ID: {nuevo.id}")
        print(self.clientes)

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
##########CLIENTES##########

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
##########PIEZAS##########

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
            print(f"Código: {maquina.code} | Descripción: {maquina.descripcion} | Requerimientos: {maquina.requerimientos}")
##########MAQUINA##########