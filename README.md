# SkyBridge Airlines - Sistema de Gestión de Logística Aérea

Este proyecto corresponde a la **Fase 1** del Trabajo Práctico Obligatorio para la solución de administración y análisis de operaciones aéreas de SkyBridge Airlines.

**Fase 1: Gestión inicial y visualización básica**
La primera versión funcional del sistema permite centralizar, registrar y navegar la información de los vuelos mediante una interfaz interactiva de consola. Las funcionalidades incluidas en esta entrega son:

**Registrar vuelo (Alta):** Permite la carga de datos de manera manual mediante consola o de forma automatizada con valores aleatorios para facilitar las pruebas.
**Eliminar vuelo (Baja):** Permite la eliminación de un vuelo del sistema mediante la validación de su código único, requiriendo confirmación del usuario y aplicando la restricción de que solo se pueden eliminar vuelos en estado "Cancelado".
**Modificar vuelo (Modificación):** Permite la búsqueda de un vuelo por su código para alterar cualquiera de sus atributos de forma individual.
**Informe General (Visualización de datos):** Muestra el listado de la totalidad de los vuelos cargados. Los mismos se presentan ordenados de mayor a menor según la cantidad de pasajeros registrados y, en caso de empate, se ordenan alfabéticamente por su ciudad de destino.

## Integrantes del Grupo y Roles:
**Tomas Gadaleta:** Menú de inicio, tipo de ingreso, generación aleatoria y ejecución principal (main).
**Santino Nasuti:** Funciones de validación de códigos e ingreso manual de datos por consola (destino, horario, pasajeros, peso, estado y tipo).
**Matias Cross:** Lógica, confirmación y opciones para la eliminación de vuelos del sistema.
**Moro Bussolini:** Opciones del menú principal, validación de rangos, generación de datos aleatorios y lógica de modificación de atributos.
**Santiago Molina:** Lógica de ordenamiento (método burbuja doble por pasajeros/destino) e informe de visualización general de datos.

## URL del Repositorio
**Repositorio Público:** https://github.com/morobussolini/Skybridge-Airlines-TPO
