class ExceptionClienteYaExiste(Exception):
    """Excepción lanzada cuando se intenta agregar un cliente que ya existe."""

    def __init__(self, dni, mensaje="El cliente ya existe."):
        self.dni = dni
        mensaje = f"{mensaje} DNI: {dni}"
        super().__init__(mensaje)


class ExceptionEmpresaYaExiste(Exception):
    """Excepción lanzada cuando se intenta agregar una empresa que ya existe."""

    def __init__(self, rut, mensaje="La empresa ya existe."):
        self.rut = rut
        mensaje = f"{mensaje} RUT: {rut}"
        super().__init__(mensaje)
