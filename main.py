import datetime

from entities.Sistema import Sistema
sistema = Sistema()

from exceptions.ExceptionClienteYaExiste import ExceptionClienteYaExiste
from exceptions.ExceptionPiezaYaExiste import ExceptionPiezaYaExiste
from exceptions.ExceptionMaquinaYaExiste import ExceptionMaquinaYaExiste


while True:
    print("\n-- MENÚ PRINCIPAL --")
    print(
        "\n1. Registrar \n2. Listar \n3. Salir del Sistema \n"
    )

    try:
        opcion1 = int(input("Ingresa el número de operación: "))
    except ValueError:
        print("Debes ingresar un número.")
        continue

    if opcion1 == 1:
        print("\n-- MENU DE REGISTRO --")
        print(
            "\n1. Pieza \n2. Máquina \n3. Cliente \n4. Pedido \n5. Reposición \n6. Salir \n"
        )
        try:
            opcion2 = int(input("Ingresa el número de operación: "))
        except ValueError:
            print("Debes ingresar un número.")
            continue
        
        if opcion2 == 1:
            print("\nRegistrar - Pieza\n")
            while True:
                try:
                    descripcion = str(input("Descripción: "))
                    for pieza in sistema.piezas:
                        if not descripcion:
                            raise ValueError("La descripción no puede estar vacía.")
                        elif pieza.descripcion == descripcion:
                            raise ExceptionPiezaYaExiste()
                    break
                except ExceptionPiezaYaExiste:
                    print(f"Ya existe una pieza con la descripción: {descripcion}")
                except ValueError:
                    print("Debes ingresar un texto válido para la descripción.")

            try:
                costo = float(input("Costo: "))
                lote = int(input("Lote: "))
                cantidad = int(input("Cantidad disponible: "))
            except ValueError:
                print("Error: Debés ingresar valores numéricos para costo, lote y cantidad.")
                continue

            pieza = sistema.registrar_pieza(descripcion, costo, lote, cantidad)
            print(f"\nPieza registrada con código {pieza.code}")

        elif opcion2 == 2:
            print("\nRegistrar - Máquina\n")
            lista_piezas = sistema.piezas.copy()
            descripcion = ""
            while True:
                if not lista_piezas:
                    break
                try:
                    descripcion = str(input("Descripción: "))
                    for maquina in sistema.maquinas:
                        if not descripcion:
                            raise ValueError()
                        if maquina.descripcion == descripcion:
                            raise ExceptionMaquinaYaExiste()
                    break
                except ExceptionMaquinaYaExiste:
                    print(f"Ya existe una máquina con la descripción: {descripcion}")
                except ValueError:
                    print("Debes ingresar un texto válido para la descripción.")
            requisitos = []
            if not lista_piezas:
                print("No es posible registrar una máquina sin piezas registradas.")
                continue
            nueva_maquina = sistema.registrar_maquina(descripcion, requisitos)
            while True:
                print("\nPiezas disponibles:")
                for pieza in lista_piezas:
                    print(f" * Código: {pieza.code} | Descripción: {pieza.descripcion}")
                try:
                    codigoPieza = int(input("\nIngresa el código de la pieza: "))
                    for pieza in lista_piezas:
                        if pieza.code == codigoPieza:
                            cantidad = int(input("Cantidad requerida: "))
                            if cantidad > 0:
                                requisitos.append(sistema.registrar_requerimiento(nueva_maquina, pieza, cantidad))
                                lista_piezas.remove(pieza)
                                print("Pieza agregada como requisito.")
                                break
                            else:
                                print("La cantidad debe ser mayor a 0.")
                                continue
                        else:
                            print("Código de pieza no encontrado.")
                    break
                except ValueError:
                    print("Debes ingresar un número.")
                    continue
            while True:
                print("\nAgregar requisito de pieza\n \n1. Si \n2. No")
                try:
                    opcion4 = int(input("\nIngresa el número de operación: "))
                except ValueError:
                    print("Debes ingresar un número.")
                    continue
                if opcion4 == 1:
                    if not lista_piezas:
                        print("No hay piezas disponibles") #si no hay piezas disponibres
                        continue
                    print("\nPiezas disponibles:")
                    for pieza in lista_piezas:
                        print(f"Código: {pieza.code} | Descripción: {pieza.descripcion}")

                    try:
                        codigoPieza = int(input("\nIngresa el código de la pieza: "))
                        for pieza in lista_piezas:
                            if pieza.code == codigoPieza:
                                cantidad = int(input("Cantidad requerida: "))
                                if cantidad > 0:
                                    requisitos.append(sistema.registrar_requerimiento(nueva_maquina, pieza, cantidad))
                                    lista_piezas.remove(pieza)
                                    print("Pieza agregada como requisito.")
                                else:
                                    print("La cantidad debe ser mayor a 0.")
                                    continue
                                break
                            print("Código de pieza no encontrado.")
                    except ValueError:
                        print("Debes ingresar un número.")
                        continue

                elif opcion4 == 2:
                    
                    print("\nMaquina agregada con exito!")
                    break
                else:
                    print("\nNúmero de operación no encontrado")

        elif opcion2 == 3:
            print("\nRegistrar - Cliente\n")
            tipo = input("Tipo de cliente (1 - Particular, 2 - Empresa): ")

            while True:
                try:
                    telefono = int(input("Teléfono: "))
                    if not telefono:
                        raise ValueError()
                except ValueError:
                    print("Debes ingtesar telefono válido.")
                    continue
                break

            while True:
                try:
                    email = str(input("Email: "))
                    if not email:
                        raise ValueError()
                    if "@" not in email or "." not in email:
                        raise ValueError()
                except ValueError:
                    print("Debes ingresar un email válido.")
                    continue
                break

            if tipo == "1":
                while True:
                    try:
                        dni = str(input("DNI: "))
                        for cliente in sistema.clientes:
                            if cliente.dni == dni:
                                raise ExceptionClienteYaExiste()
                        break
                    except ValueError:
                        print("Debes ingresar un número válido para el DNI.")
                    except ExceptionClienteYaExiste:
                        print("Ya existe un cliente con el DNI: {dni}")
                nombre = input("Nombre completo: ")
                cliente = sistema.registrar_cliente_particular(telefono, email, dni, nombre)
                print(f"\nCliente particular registrado con ID {cliente.id}")

            elif tipo == "2":
                while True:
                    try:
                        rut = str(input("RUT: "))
                        for cliente in sistema.clientes:
                            if cliente.tipo_cliente == "Empresa" and cliente.rut == rut:
                                raise ExceptionClienteYaExiste()
                        break
                    except ValueError:
                        print("Debes ingresar un número válido para el RUT.")
                    except ExceptionClienteYaExiste:
                        print(f"Ya existe un cliente con el RUT: {rut}")

                nombre = str(input("Nombre de empresa: "))
                
                # web = str(input("Sitio web: "))
                while True:
                    try:
                        web = str(input("Sitio web: "))
                        if not web:
                            raise ValueError()
                        if "." not in web:
                            raise ValueError()
                        break
                    except ValueError:
                        print("Debes ingresar un sitio web válido.")
                        continue
                cliente = sistema.registrar_cliente_empresa(telefono, email, rut, nombre, web)
                print(f"\nCliente empresa registrado con ID {cliente.id}")

            else:
                print("\nTipo de cliente inválido.")

        elif opcion2 == 4:
            print("\nRegistrar - Pedido\n")

            sistema.listar_clientes()
            try:
                cliente_pedido = int(input("Ingresa el ID del cliente: "))
                for cliente in sistema.clientes:
                    if cliente.id == cliente_pedido:
                        cliente_pedido = cliente
                    else:
                        print("ID de cliente no encontrado.")
                        continue
            except ValueError:
                print("Debes ingresar un número válido para el ID del cliente.")
                continue

            sistema.listar_maquinas()
            try:
                codigo_maquina = int(input("Ingresa el código de la máquina: "))
                for maquina in sistema.maquinas:
                    if maquina.code == codigo_maquina:
                        codigo_maquina = maquina
                    else:
                        print("Código de máquina no encontrado.")
                        continue
            except ValueError:
                print("Debes ingresar un número válido para el código de la máquina.")
                continue
            fecha_recibido = datetime.datetime.now()
            fecha_entregado = None
            estado = "Pendiente"
            pedido = sistema.registrar_pedido(cliente_pedido, codigo_maquina, fecha_recibido, fecha_entregado, estado)
            print(f"\nPedido registrado para el cliente {cliente_pedido.nombre} y la máquina {maquina.descripcion}")

        elif opcion2 == 5:
            print("\nRegistrar - Reposición\n")
            if not sistema.piezas:
                print("No hay piezas registradas - Volviendo al menú principal")
                continue
            sistema.listar_piezas()
            try:
                codigo_pieza = int(input("Ingresa el código de la pieza a reponer: "))
                for pieza in sistema.piezas:
                    if pieza.code == codigo_pieza:
                        cantidad_lotes = int(input("Cantidad de lotes a reponer: "))
                        if cantidad_lotes > 0:
                            fecha_reposicion = datetime.datetime.now()
                            repo = sistema.generar_reposicion(pieza, cantidad_lotes, fecha_reposicion)
                            print(f"\nReposicion finalizada. \n * Costo total de reposicion: ${repo}\n * Nueva cantidad de {pieza.descripcion}: {pieza.cantidad} unidades")
                        else:
                            print("La cantidad debe ser mayor a 0.")
                        break
                    else:
                        print("Código de pieza no encontrado.")
                        continue
            except ValueError:
                print("Debes ingresar un número.")
                continue

        elif opcion2 == 6:
            continue
        else:
            print("\nNúmero de operación no encontrado - Volviendo al menú principal")

    elif opcion1 == 2:
        print("\n-- MENU DE LISTADO --")
        print(
            "\n1. Clientes \n2. Pedidos \n3. Máquinas \n4. Piezas \n5. Contabilidad \n6. Salir \n"
        )
        try:
            opcion3 = int(input("Ingresa el número de operación: "))
        except ValueError:
            print("Debes ingresar un número.")
            continue
        
        if opcion3 == 1:
            print("\nListar - Clientes\n")
            sistema.listar_clientes()

        elif opcion3 == 2:
            print("\nListar - Pedidos\n")
            sistema.listar_pedidos()

        elif opcion3 == 3:
            print("\nListar - Máquinas\n")
            sistema.listar_maquinas()

        elif opcion3 == 4:
            print("\nListar - Piezas\n")
            sistema.listar_piezas() 

        elif opcion3 == 5:
            print("\nListar - Contabilidad\n")
            sistema.listar_contabilidad()

        elif opcion3 == 6:
            continue
        else:
            print("\nNúmero de operación no encontrado - Volviendo al menú principal")

    elif opcion1 == 3:
        print("Saliendo del sistema...")
        break
    else:
        print("\nNúmero de operación no encontrado - Volviendo al menú principal")