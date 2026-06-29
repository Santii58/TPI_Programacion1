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
        while nueva_poblacion is None:
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
            
        # Pedir nueva superficie
        
        nueva_superficie = None
        while nueva_superficie is None:
            try:
                entrada = input("Ingrese la nueva superficie (km²): ").strip()
                superficie_int = int(entrada)
                if superficie_int > 0:
                    nueva_superficie = entrada
                else:
                    print("⚠ Error: La superficie debe ser un número positivo. Intente nuevamente.")
            except ValueError:
                print("⚠ Error: La superficie debe ser un número entero. Intente nuevamente.")
            except Exception as e:
                print(f"⚠ Error inesperado al ingresar la superficie: {e}. Intente nuevamente.")
            # Actualizar datos en la fila
        if len(filas[indice_pais]) >= 3:
            filas[indice_pais][1] = nueva_poblacion
            filas[indice_pais][2] = nueva_superficie 
         # Guardar cambios en el archivo
        try:
            with open('paises.csv', 'w', newline='', encoding='utf-8') as archivo:
                escritor = csv.writer(archivo)
                escritor.writerows(filas)
            print(f"✓ Datos del país '{nombre_pais}' actualizados exitosamente.")
        except IOError as e:
            print(f"Error al escribir en el archivo: {e}")
        except Exception as e:
            print(f"Error inesperado al guardar los cambios: {e}")
    
    except KeyboardInterrupt:
        print("\n⚠ Operación cancelada por el usuario.")
    except Exception as e:
        print(f"Error general: {e}")
           

def buscar_pais():
    """Busca un país por nombre con coincidencia parcial o exacta"""
    try:
        # Pedir nombre del país a buscar
        nombre_buscar = None
        while nombre_buscar is None:
            try:
                nombre_buscar = input("Ingrese el nombre del país a buscar: ").strip()
                if not nombre_buscar:
                    print("⚠ Error: El nombre no puede estar vacío. Intente nuevamente.")
                    nombre_buscar = None
            except Exception as e:
                print(f"⚠ Error al ingresar el nombre: {e}. Intente nuevamente.")
                nombre_buscar = None
        
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
        
        # Buscar coincidencias
        coincidencias = []
        nombre_lower = nombre_buscar.lower()
        
        for fila in filas:
            if len(fila) > 0:
                nombre_pais = fila[0].lower()
                # Buscar coincidencia exacta o parcial
                if nombre_pais == nombre_lower or nombre_lower in nombre_pais:
                    coincidencias.append(fila)
        
        # Mostrar resultados
        if coincidencias:
            print(f"\n✓ Se encontraron {len(coincidencias)} resultado(s):\n")
            print(f"{'Nombre':<20} {'Población':<15} {'Superficie':<15} {'Continente':<15}")
            print("-" * 65)
            
            for pais in coincidencias:
                if len(pais) >= 4:
                    print(f"{pais[0]:<20} {pais[1]:<15} {pais[2]:<15} {pais[3]:<15}")
                else:
                    print(f"{pais[0]:<20} {'N/A':<15} {'N/A':<15} {'N/A':<15}")
        else:
            print(f"⚠ No se encontraron países con el nombre '{nombre_buscar}'")
    
    except KeyboardInterrupt:
        print("\n⚠ Operación cancelada por el usuario.")
    except Exception as e:
        print(f"Error general: {e}")

def filtrar_paises():
    """Filtra países por continente, rango de población o rango de superficie"""
    try:
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
 
        if not filas:
            print("⚠ El archivo no contiene datos.")
            return
 
        # Mostrar opciones de filtro

        print("\n¿Por qué criterio desea filtrar?")
        print("  1. Por continente")
        print("  2. Por rango de población")
        print("  3. Por rango de superficie")
 
        opcion = None
        while opcion is None:
            try:
                entrada = input("Seleccione una opción (1-3): ").strip()
                if entrada in ("1", "2", "3"):
                    opcion = entrada
                else:
                    print("⚠ Opción inválida. Ingrese 1, 2 o 3.")
            except Exception as e:
                print(f"⚠ Error al leer la opción: {e}. Intente nuevamente.")
 
        resultado = []
 
        # Filtro por continente

        if opcion == "1":
            continente_buscar = None
            while continente_buscar is None:
                try:
                    continente_buscar = input("Ingrese el continente: ").strip()
                    if not continente_buscar:
                        print("⚠ El continente no puede estar vacío. Intente nuevamente.")
                        continente_buscar = None
                except Exception as e:
                    print(f"⚠ Error: {e}. Intente nuevamente.")
                    continente_buscar = None
 
            for fila in filas:
                if len(fila) >= 4 and fila[3].lower() == continente_buscar.lower():
                    resultado.append(fila)
 
        # Filtro por rango de población

        elif opcion == "2":
            pob_min = None
            while pob_min is None:
                try:
                    entrada = input("Ingrese la población mínima: ").strip()
                    valor = int(entrada)
                    if valor >= 0:
                        pob_min = valor
                    else:
                        print("⚠ El valor debe ser mayor o igual a 0.")
                except ValueError:
                    print("⚠ Error: Ingrese un número entero.")
                except Exception as e:
                    print(f"⚠ Error inesperado: {e}. Intente nuevamente.")
 
            pob_max = None
            while pob_max is None:
                try:
                    entrada = input("Ingrese la población máxima: ").strip()
                    valor = int(entrada)
                    if valor >= pob_min:
                        pob_max = valor
                    else:
                        print(f"⚠ El máximo debe ser mayor o igual al mínimo ({pob_min}).")
                except ValueError:
                    print("⚠ Error: Ingrese un número entero.")
                except Exception as e:
                    print(f"⚠ Error inesperado: {e}. Intente nuevamente.")
 
            for fila in filas:
                if len(fila) >= 2:
                    try:
                        pob = int(fila[1])
                        if pob_min <= pob <= pob_max:
                            resultado.append(fila)
                    except ValueError:
                        pass
 
        # Filtro por rango de superficie

        elif opcion == "3":
            sup_min = None
            while sup_min is None:
                try:
                    entrada = input("Ingrese la superficie mínima (km²): ").strip()
                    valor = int(entrada)
                    if valor >= 0:
                        sup_min = valor
                    else:
                        print("⚠ El valor debe ser mayor o igual a 0.")
                except ValueError:
                    print("⚠ Error: Ingrese un número entero.")
                except Exception as e:
                    print(f"⚠ Error inesperado: {e}. Intente nuevamente.")
 
            sup_max = None
            while sup_max is None:
                try:
                    entrada = input("Ingrese la superficie máxima (km²): ").strip()
                    valor = int(entrada)
                    if valor >= sup_min:
                        sup_max = valor
                    else:
                        print(f"⚠ El máximo debe ser mayor o igual al mínimo ({sup_min}).")
                except ValueError:
                    print("⚠ Error: Ingrese un número entero.")
                except Exception as e:
                    print(f"⚠ Error inesperado: {e}. Intente nuevamente.")
 
            for fila in filas:
                if len(fila) >= 3:
                    try:
                        sup = int(fila[2])
                        if sup_min <= sup <= sup_max:
                            resultado.append(fila)
                    except ValueError:
                        pass
 
        # Mostrar resultados

        if resultado:
            print(f"\n✓ Se encontraron {len(resultado)} país/es:\n")
            print(f"{'Nombre':<20} {'Población':<15} {'Superficie':<15} {'Continente':<15}")
            print("-" * 65)
            for pais in resultado:
                if len(pais) >= 4:
                    print(f"{pais[0]:<20} {pais[1]:<15} {pais[2]:<15} {pais[3]:<15}")
        else:
            print("⚠ No se encontraron países con ese criterio.")
 
    except KeyboardInterrupt:
        print("\n⚠ Operación cancelada por el usuario.")
    except Exception as e:
        print(f"Error general: {e}")

def ordenar_paises():
    """Ordena y muestra los países según criterio y dirección elegidos"""
    try:
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
 
        if not filas:
            print("⚠ El archivo no contiene datos.")
            return
 
        # Elegir criterio de ordenamiento

        print("\n¿Por qué criterio desea ordenar?")
        print("  1. Por nombre (A-Z / Z-A)")
        print("  2. Por población")
        print("  3. Por superficie")
 
        criterio = None
        while criterio is None:
            try:
                entrada = input("Seleccione una opción (1-3): ").strip()
                if entrada in ("1", "2", "3"):
                    criterio = entrada
                else:
                    print("⚠ Opción inválida. Ingrese 1, 2 o 3.")
            except Exception as e:
                print(f"⚠ Error: {e}. Intente nuevamente.")
 
        # Elegir direccion

        print("\n¿En qué dirección?")
        print("  1. Ascendente")
        print("  2. Descendente")
 
        direccion = None
        while direccion is None:
            try:
                entrada = input("Seleccione una opción (1-2): ").strip()
                if entrada in ("1", "2"):
                    direccion = entrada
                else:
                    print("⚠ Opción inválida. Ingrese 1 o 2.")
            except Exception as e:
                print(f"⚠ Error: {e}. Intente nuevamente.")
 
        invertir = (direccion == "2")
 
        # Ordenar segun criterio

        try:
            if criterio == "1":
                filas_ordenadas = sorted(filas, key=lambda f: f[0].lower() if len(f) > 0 else "", reverse=invertir)
            elif criterio == "2":
                filas_ordenadas = sorted(filas, key=lambda f: int(f[1]) if len(f) > 1 and f[1].isdigit() else 0, reverse=invertir)
            elif criterio == "3":
                filas_ordenadas = sorted(filas, key=lambda f: int(f[2]) if len(f) > 2 and f[2].isdigit() else 0, reverse=invertir)
        except Exception as e:
            print(f"⚠ Error al ordenar los datos: {e}")
            return
 
        # Mostrar resultados

        direccion_texto = "descendente" if invertir else "ascendente"
        criterio_texto = {"1": "nombre", "2": "población", "3": "superficie"}[criterio]
        print(f"\n✓ Países ordenados por {criterio_texto} ({direccion_texto}):\n")
        print(f"{'Nombre':<20} {'Población':<15} {'Superficie':<15} {'Continente':<15}")
        print("-" * 65)
        for pais in filas_ordenadas:
            if len(pais) >= 4:
                print(f"{pais[0]:<20} {pais[1]:<15} {pais[2]:<15} {pais[3]:<15}")
 
    except KeyboardInterrupt:
        print("\n⚠ Operación cancelada por el usuario.")
    except Exception as e:
        print(f"Error general: {e}")
def mostrar_estadisticas():
    pass
