#PROGRAMA PRINCIPAL
import modulos

while True:
    try:
        print("!!!MENU PRINCIPAL¡¡¡")
        print("Opcion 1:Agregar pais")
        print("Opcion 2:Actualizar datos(Poblacion y superficie)")
        print("Opcion 3:Buscar un pais")
        print("Opcion 4:Filtrar paises")
        print("Opcion 5:Ordenar paises")
        print("Opcion 6:Mostrar estadisticas")
        print("Opcion 7:Salir")
        opcion = int(input("Seleccione una opcion:"))
        if opcion == 1:
            modulos.agregar_pais()
        elif opcion == 2:
            modulos.actualizar_datos()
        elif opcion == 3:
            modulos.buscar_pais()
        elif opcion == 4:
            modulos.filtrar_paises()
        elif opcion == 5:
            modulos.ordenar_paises()
        elif opcion == 6:
            modulos.mostrar_estadisticas()
        elif opcion == 7:
            break
        else:
            raise ValueError ("Ingrese una opcion valida")
    except ValueError as e:
        print(f"{e}")
    except Exception:
        print("ERRO INESPERADO")
                   
     