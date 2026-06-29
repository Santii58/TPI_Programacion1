#FUNCIONES DEL PROGRAMA









#MENU PRINCIPAL


while True:
    try:
        print("Bienvenido al programa principal")
        print("1. Opción 1")
        print("2. Opción 2")
        print("3. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            # Llamar a la función correspondiente a la opción 1
            pass
        elif opcion == 2:
            # Llamar a la función correspondiente a la opción 2
            pass
        elif opcion == 3:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")