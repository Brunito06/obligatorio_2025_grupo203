from entities import Cliente , Pieza , Maquina , Reposicion ,  Requerimiento , Sistema

print(
    "1. Registrar \n2. Listar \n3. Salir del Sistema \n"
)

opcion1 = int(input("Ingresa el número de operación: "))

if opcion1 == 1:
    print(
        "1. Pieza \n2. Máquina \n3. Cliente \n4. Pedido \n5. Reposición \n6. Salir "
    )
    opcion2 = int(input("Ingresa el número de operación: "))
    if opcion2 == 1:
        Pieza.saludar("Juan")

elif opcion1 == 2:
    print(
        "1. Clientes \n2. Pedidos \n3. Máquinas \n4. Piezas \n5. Contabilidad \n26. Salir "
    )