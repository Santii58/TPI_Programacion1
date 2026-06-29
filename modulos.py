# MODULOS DEL PROGRAMA
import csv

def agregar_pais():
    """Abre el archivo CSV y agrega un nuevo país con sus datos"""
    try:
        # Validar nombre
        nombre = None
        while nombre is None:
            try:
                nombre = input("Ingrese el nombre del país: ").strip()
                if not nombre:
                    print("⚠ Error: El nombre no puede estar vacío. Intente nuevamente.")
                    nombre = None
            except Exception as e:
                print(f"⚠ Error al ingresar el nombre: {e}. Intente nuevamente.")
                nombre = None
        
        # Validar población
        poblacion = None
        while poblacion is None:
            try:
                entrada = input("Ingrese la población: ").strip()
                poblacion_int = int(entrada)
                if poblacion_int > 0:
                    poblacion = entrada
                else:
                    print("⚠ Error: La población debe ser un número positivo. Intente nuevamente.")
            except ValueError:
                print("⚠ Error: La población debe ser un número entero. Intente nuevamente.")
            except Exception as e:
                print(f"⚠ Error inesperado al ingresar la población: {e}. Intente nuevamente.")
        
        # Validar superficie
        superficie = None
        while superficie is None:
            try:
                entrada = input("Ingrese la superficie (km²): ").strip()
                superficie_int = int(entrada)
                if superficie_int > 0:
                    superficie = entrada
                else:
                    print("⚠ Error: La superficie debe ser un número positivo. Intente nuevamente.")
            except ValueError:
                print("⚠ Error: La superficie debe ser un número entero. Intente nuevamente.")
            except Exception as e:
                print(f"⚠ Error inesperado al ingresar la superficie: {e}. Intente nuevamente.")
        
        # Validar continente
        continente = None
        while continente is None:
            try:
                continente = input("Ingrese el continente: ").strip()
                if not continente:
                    print("⚠ Error: El continente no puede estar vacío. Intente nuevamente.")
                    continente = None
            except Exception as e:
                print(f"⚠ Error al ingresar el continente: {e}. Intente nuevamente.")
                continente = None
        
        # Abrir archivo CSV en modo append
        try:
            with open('paises.csv', 'a', newline='', encoding='utf-8') as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow([nombre, poblacion, superficie, continente])
            print(f"✓ País '{nombre}' agregado exitosamente al archivo.")
        except FileNotFoundError:
            print("Error: No se encontró el archivo paises.csv")
        except IOError as e:
            print(f"Error al escribir en el archivo: {e}")
        except Exception as e:
            print(f"Error inesperado al guardar el país: {e}")
    
    except KeyboardInterrupt:
        print("\n⚠ Operación cancelada por el usuario.")
    except Exception as e:
        print(f"Error general: {e}")

def actualizar_datos():
    """Actualiza población y superficie de un país existente"""
    try:
        # Pedir nombre del país
        nombre_pais = None
        while nombre_pais is None:
            try:
                nombre_pais = input("Ingrese el nombre del país a modificar: ").strip()
                if not nombre_pais:
                    print("⚠ Error: El nombre no puede estar vacío. Intente nuevamente.")
                    nombre_pais = None
                if nombre_pais.isdigit:
                    raise ValueError ("El nombre de un pais no puede ser un numero")
            except Exception as e:
                print(f"⚠ Error al ingresar el nombre: {e}. Intente nuevamente.")
                nombre_pais = None
    # Leer archivo CSV
        try:
            with open('paises.csv', 'r', newline='', encoding='utf-8') as archivo:
                lector = csv.reader(archivo)
                filas = list(lector)
        except FileNotFoundError:
            print("Error: No se encontró el archivo paises.csv")
            return
        except IOError as e:
            print(f"Error al leer el archivo: {e}")
            return
        except Exception as e:
            print(f"Error inesperado al leer el archivo: {e}")
            return
        
        # Buscar el país
        
        pais_encontrado = False
        indice_pais = -1
        
        for i, fila in enumerate(filas):
            if len(fila) > 0 and fila[0].lower() == nombre_pais.lower():
                pais_encontrado = True
                indice_pais = i
                break
        
        if not pais_encontrado:
            print(f"⚠ Error: No se encontró el país '{nombre_pais}' en el archivo.")
            return
        
        #pedir nueva poblacion
        nueva_poblacion = None
        while nueva_poblacion is None
        try:
            entrada = input("Ingrese la nueva població: ").strip()
            poblacion_int = int(entrada)
            if poblacion_int > 0:
                nueva_poblacion = entrada
            else:
                print("⚠ Error: La población debe ser un número positivo. Intente nuevamente.")
        except ValueError:
            print("⚠ Error: La población debe ser un número entero. Intente nuevamente.")
        except Exception as e:
            print(f"⚠ Error inesperado al ingresar la población: {e}. Intente nuevamente.")
                
    

def buscar_pais():
    pass

def filtrar_paises():
    pass

def ordenar_paises():
    pass

def mostrar_estadisticas():
    pass
