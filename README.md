Biblioteca de Manipulación de Bases de Datos SQLite
Este código en Python proporciona una herramienta simple para crear y gestionar bases de datos SQLite, especialmente diseñada para el contexto de una biblioteca. Esta biblioteca permite a los usuarios definir tablas personalizadas con columnas específicas y luego insertar datos en ellas de manera interactiva.

Características
Creación de Tablas Dinámicas: La función crea_bbdd facilita la creación dinámica de tablas en una base de datos SQLite. Los usuarios pueden definir el nombre de la tabla y las columnas junto con sus tipos de datos.

Generación de Diccionarios de Columnas: La función crea_diccionario_columnas permite a los usuarios especificar la cantidad de columnas y definir sus nombres y tipos de datos de manera interactiva.

Inserción de Datos Interactiva: La función inserta_datos permite a los usuarios insertar datos en la tabla creada de manera interactiva, solicitando valores para cada columna.

Ejemplo de Uso
python
Copy code
import sqlite3

# Crear una tabla dinámicamente
def crea_bbdd(nombre_tabla, columnas):
    # Código de creación de la tabla ...

# Generar un diccionario de columnas de manera interactiva
def crea_diccionario_columnas():
    # Código para crear el diccionario de columnas ...

# Insertar datos de manera interactiva en la tabla creada
def inserta_datos(nombre_tabla, columnas):
    # Código de inserción de datos ...

if __name__ == "__main__":
    # Ejecutar el programa principal ...

    # Solicitar el nombre de la tabla y generar el diccionario de columnas
    nombre_tabla = input('Introduce nombre de la tabla: ')
    diccionario_columnas = crea_diccionario_columnas()

    # Crear la tabla en la base de datos
    crea_bbdd(nombre_tabla, diccionario_columnas)

    # Solicitar la inserción de datos en la tabla creada
    insert = input('¿Quieres introducir datos en la tabla creada? ')
    if insert.lower() == 'si':
        while True:
            inserta_datos(nombre_tabla, diccionario_columnas)
            seguir = input('¿Quieres introducir más datos (si/no): ')
            if seguir.lower() != 'si':
                break
Este código proporciona una interfaz interactiva para crear tablas SQLite personalizadas y agregar datos a ellas de manera fácil y eficiente. Además, permite a los usuarios definir la estructura de la base de datos según sus necesidades específicas.






