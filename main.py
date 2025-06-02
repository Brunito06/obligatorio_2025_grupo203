from entities.Sistema import Sistema

sistema = Sistema()

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
        print("\n-- MENU DE REGISTRACIÓN --")
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
            descripcion = input("Descripción: ")
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
            descripcion = input("Descripción: ")
            requisitos = []
            while True:
                print("\nAgregar requisito del pieza\n \n1. Si \n2. No")
                try:
                    opcion4 = int(input("\nIngresa el número de operación: "))
                except ValueError:
                    print("Debes ingresar un número.")
                    continue
                if opcion4 == 1:
                    
                    # Lista de piezas disponibles
                    lista_piezas = sistema.piezas.copy()
                    if not lista_piezas:
                        print("No hay piezas disponibles") #si no hay piezas disponibres
                        continue
                    for pieza in lista_piezas:
                        if pieza.code in requisitos:
                            lista_piezas.remove(pieza) #si el codigo de la pieza ya está en requisitos, no lo muestra
                    print("\nPiezas disponibles:")
                    for pieza in lista_piezas:
                        print(f"Código: {pieza.code} | Descripción: {pieza.descripcion}")

                    try:
                        codigoPieza = int(input("\nIngresa el código de la pieza: "))
                        for pieza in sistema.piezas:
                            if pieza.code == codigoPieza:
                                requisitos.append(pieza.code)
                                print("Pieza agregada como requisito.")
                                break
                    except ValueError:
                        print("Debes ingresar un número.")
                        continue

                elif opcion4 == 2:
                    sistema.registrar_maquina(descripcion, requisitos)
                    print("\nMaquina agregada con exito!")
                    break
                else:
                    print("\nNúmero de operación no encontrado")

        elif opcion2 == 3:
            print("\nRegistrar - Cliente\n")
            tipo = input("Tipo de cliente (1 - Particular, 2 - Empresa): ")

            telefono = input("Teléfono: ")
            email = input("Email: ")

            if tipo == "1":
                dni = input("DNI: ")
                nombre = input("Nombre completo: ")
                cliente = sistema.registrar_cliente_particular(telefono, email, dni, nombre)
                print(f"\nCliente particular registrado con ID {cliente.id}")

            elif tipo == "2":
                rut = input("RUT: ")
                nombre = input("Nombre de empresa: ")
                web = input("Sitio web: ")
                cliente = sistema.registrar_cliente_empresa(telefono, email, rut, nombre, web)
                print(f"\nCliente empresa registrado con ID {cliente.id}")

            else:
                print("\nTipo de cliente inválido.")

        elif opcion2 == 4:
            print("\nRegistrar - Pedido\n")

        elif opcion2 == 5:
            print("\nRegistrar - Reposición\n")

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
            #sistema.listar_pedidos()

        elif opcion3 == 3:
            print("\nListar - Máquinas\n")
            sistema.listar_maquinas()

        elif opcion3 == 4:
            print("\nListar - Piezas\n")
            sistema.listar_piezas() 

        elif opcion3 == 5:
            print("\nListar - Contabilidad\n")
            #sistema.listar_contabilidad()

        elif opcion3 == 6:
            continue
        else:
            print("\nNúmero de operación no encontrado - Volviendo al menú principal")

    elif opcion1 == 3:
        print("Saliendo del sistema...")
        break
    else:
        print("\nNúmero de operación no encontrado - Volviendo al menú principal")