from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, id, telefono, email):
        self.id = id
        self.telefono = telefono
        self.email = email
    
    @abstractmethod
    def tipo_cliente(self):
        pass

class ClienteParticular(Cliente):
    def __init__(self, id , telefono, email, dni, nombre):
        super().__init__(id , telefono, email)
        self.dni = dni
        self.nombre = nombre

    def tipo_cliente(self):
        return "Particular"

class ClienteEmpresa(Cliente):
    def __init__(self, id, telefono, email, rut, nombre, web):
        super().__init__(id, telefono, email)
        self.rut = rut
        self.nombre = nombre
        self.web = web

    def tipo_cliente(self):
        return "Empresa"
