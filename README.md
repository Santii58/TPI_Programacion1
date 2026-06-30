# Gestión de Datos de Países en Python

TPI — Programación 1 | Tecnicatura Universitaria en Programación (UTN)

# Descripción

Aplicación de consola en Python que permite gestionar un dataset de países cargado desde un archivo CSV. Implementa búsquedas, filtros, ordenamientos y estadísticas haciendo uso de listas, diccionarios y funciones modularizadas.

## Estructura del proyecto

```
├── main.py          # Código fuente principal
├── paises.csv       # Dataset base (49 países)
├── README.md        # Este archivo
└── informe.pdf      # Documentación académica y técnica
```

## Funcionalidades

| Opción | Descripción |
|--------|-------------|
| 1 | Agregar un nuevo país (sin campos vacíos ni duplicados) |
| 2 | Actualizar población y/o superficie de un país existente |
| 3 | Buscar país por nombre (coincidencia parcial, ignora mayúsculas) |
| 4 | Filtrar por continente, rango de población o rango de superficie |
| 5 | Ordenar por nombre, población o superficie (asc/desc) |
| 6 | Estadísticas: máximos, mínimos, promedios y conteo por continente |
| 7 | Salir del Programa |



# Ejemplos de uso

# Agregar un país

Ingresá una opción: 1
Nombre del país: Japón
Población: 125800000
Superficie (km²): 377975
Continente: Asia
[OK] 'Japón' agregado correctamente.
```

### Buscar por nombre
```
Ingresá una opción: 3
Texto a buscar en el nombre: ar
Se encontraron 3 resultado(s):

NOMBRE               POBLACIÓN  SUPERFICIE (km²) CONTINENTE

Argentina           45,376,763         2,780,400 América
Bulgaria             6,520,000            110,879 Europa
Marruecos           37,344,795           710,850 África

```

### Estadísticas
```
Ingresá una opción: 6
  Total de países cargados : 49
  Mayor población          : China (1,412,600,000 hab.)
  Menor población          : Uruguay (3,574,964 hab.)
  Promedio de población    : 143,526,789 hab.
  Promedio de superficie   : 1,686,542 km²

  Países por continente:
    África               9 país/es
    América              15 país/es
    Asia                 12 país/es
    Europa               12 país/es
    Oceanía              3 país/es
```

---

## Formato del CSV

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
```

---

## Validaciones implementadas

- Campos vacíos no permitidos al agregar
- Nombres duplicados detectados (insensible a mayúsculas)
- Valores numéricos negativos rechazados
- Errores de formato en el CSV reportados por línea sin detener la ejecución
- Filtros con rango inválido (mínimo > máximo) detectados
- Búsquedas sin resultados informadas con mensaje claro

---

## Integrantes

|Nombre| Legajo |
|--------|--------|
| [Tomas Ñanculeu] | [ 36529] |
| [Santiago Nervi] | [ 7225 ] |

## Docentes 
-- Sofia Elizabeth Fernández --
-- Ana Eugenia Mutti --

## Links de youtube
https://www.youtube.com/watch?v=9-eXX3Tw0o4

## Extenciones recomendadas
--@id:tomoki1207.pdf : para leer el archivo pdf desde VSC
