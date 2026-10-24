# ✈️ Sistema de Gestión Aeroportuaria

Aplicación de consola en **Python** para administrar los vuelos de un aeropuerto: registrar, buscar, eliminar y consultar vuelos, ver un panel tipo aeropuerto, calcular estadísticas y guardar los datos en un archivo de texto.

Proyecto educativo que practica programación orientada a objetos, validación de datos, manejo de archivos y modularización.

## 🎯 Funcionalidades

- **Registrar vuelos** con código, aerolínea, destino, hora, puerta, estado, pasajeros y capacidad.
- **Generación automática** de código de vuelo (`VL100`–`VL999`) y de puerta de abordaje (1–30), sin repetidos.
- **Buscar y eliminar** vuelos por código (pide confirmación si el vuelo no está cancelado ni finalizado).
- **Listado completo** y **panel de vuelos** en formato de tabla compacta.
- **Estadísticas:** total y promedio de pasajeros, vuelo con mayor ocupación y conteo por estado.
- **Guardar y consultar** los vuelos en `vuelos.txt`.
- **Información del sistema** (sistema operativo, versión de Python, etc.).

## ✅ Validaciones

- Campos de texto que no pueden quedar vacíos.
- Hora en formato `HH:MM` dentro de rangos válidos.
- Estados permitidos: `programado`, `abordando`, `retrasado`, `cancelado`, `finalizado`.
- Códigos y puertas únicos.
- Los pasajeros no pueden superar la capacidad del avión.
- Manejo de errores de conversión y de lectura o escritura de archivos.

## 🗂️ Estructura del proyecto

```
SistemaGestionAeropuerto/
├── main.py            # Menú principal y ciclo del programa
├── gestor_vuelos.py   # Lógica del sistema (funciones)
├── vuelo.py           # Clase Vuelo (POO)
├── vuelos.txt         # Archivo de ejemplo con vuelos guardados
└── README.md
```

## 🛠️ Tecnologías y conceptos

- **Python 3** (solo biblioteca estándar: `math`, `random`, `platform`).
- **POO:** clase `Vuelo` con cálculo de ocupación y formato de salida.
- **Estructuras de datos:** lista de diccionarios para almacenar los vuelos.
- **Archivos:** lectura y escritura con `open()` y manejo de excepciones.
- **Modularización:** separación entre menú, lógica y modelo.

## ▶️ Cómo ejecutarlo

1. Instala [Python 3](https://www.python.org/downloads/).
2. Clona el repositorio:
   ```bash
   git clone https://github.com/Reymonth777x/SistemaGestionAeropuerto.git
   cd SistemaGestionAeropuerto
   ```
3. Ejecuta el programa:
   ```bash
   python main.py
   ```

## 📋 Menú principal

```
1. Registrar vuelo
2. Buscar vuelo
3. Eliminar vuelo
4. Mostrar todos los vuelos
5. Ver panel de vuelos
6. Ver estadísticas
7. Guardar vuelos en archivo
8. Consultar archivo de vuelos
9. Ver información del sistema
10. Salir
```

## 🚀 Posibles mejoras

- Cargar los vuelos guardados al iniciar el programa.
- Guardar en formato JSON o CSV en lugar de texto plano.
- Agregar pruebas automáticas con `unittest` o `pytest`.
- Editar vuelos existentes.
- Migrar a una base de datos (SQLite).

## 👤 Autor

**Reymonth Enríquez Selvas**
[GitHub](https://github.com/Reymonth777x) · [LinkedIn](https://www.linkedin.com/in/reymonth-enr%C3%ADquez-selvas-37221b40)
