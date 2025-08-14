
# Sistema de Citas - Simulación en Consola

Este proyecto es una simulación en Python de un sistema de citas que permite registrar ciudadanos, asignar turnos y organizar el orden de atención según prioridad y tiempo estimado.
La interacción se realiza completamente por consola y los datos se almacenan en listas en memoria para pruebas de backend.

# Características

Registro de ciudadanos con:

- Nombre

- Tiempo estimado de atención (ingresado por el ciudadano)

- Prioridad especial (adulto mayor, persona con discapacidad, embarazada, etc.)

Asignación automática de turno único.

Ordenamiento de lista:

- Primero ciudadanos con prioridad especial (ordenados por menor tiempo estimado).

- Luego el resto de ciudadanos (también ordenados por menor tiempo estimado).

Cálculo de métricas:

- Tiempo total de atención.

- Tiempo promedio de espera.

Visualización de lista final en consola.

# Requisitos

- Python 3.8 o superior
- No requiere librerías externas.

# Ejecución

1. Clonar o descargar este repositorio.

2. Abrir una terminal en la carpeta del proyecto.

3. Ejecutar:

~~~bash  
python sistema_citas.py
~~~

4. Seguir las instrucciones en consola para ingresar los datos.


~~~bash  
Ingrese el número de ciudadanos: 3

--- Registro del ciudadano 1 ---
Nombre: Juan Pérez
Tiempo estimado (minutos): 30
¿Tiene prioridad especial? (s/n): s

--- Registro del ciudadano 2 ---
Nombre: Ana López
Tiempo estimado (minutos): 25
¿Tiene prioridad especial? (s/n): n

--- Registro del ciudadano 3 ---
Nombre: Luis Gómez
Tiempo estimado (minutos): 40
¿Tiene prioridad especial? (s/n): s

--- Lista Final ---
Turno | Nombre      | Tiempo Estimado | Prioridad
1     | Ana López   | 25              | No
2     | Juan Pérez  | 30              | Sí
3     | Luis Gómez  | 40              | Sí

Tiempo total de atención: 95 minutos
Tiempo promedio de espera: 31.67 minutos
~~~

#Notas

- Este programa es únicamente una prueba de backend en consola.
- No almacena datos en base de datos.
- En una implementación real, el código se integraría con una API o sistema de gestión de citas.
