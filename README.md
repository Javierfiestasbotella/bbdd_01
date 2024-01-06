Biblioteca de Manipulación de Bases de Datos SQLite
Este código en Python proporciona una herramienta simple para crear y gestionar bases de datos SQLite, especialmente diseñada para el contexto de una biblioteca. Esta biblioteca permite a los usuarios definir tablas personalizadas con columnas específicas y luego insertar datos en ellas de manera interactiva.

Características
Creación de Tablas Dinámicas:
La biblioteca ofrece una interfaz para crear dinámicamente tablas en una base de datos SQLite. Los usuarios pueden definir el nombre de la tabla y las columnas junto con sus tipos de datos.

Generación de Diccionarios de Columnas:
La biblioteca proporciona una función para generar diccionarios de columnas de manera interactiva. Esto permite a los usuarios especificar la cantidad de columnas y definir sus nombres y tipos de datos.

Inserción de Datos Interactiva:
La función de inserción de datos permite a los usuarios insertar datos en la tabla creada de manera interactiva, solicitando valores para cada columna.

Ejemplo de Uso con Clase Bbdd
python
Copy code
from bbdd import Bbdd

# Instanciar la clase
bbdd = Bbdd()

# Crear la base de datos y la tabla
bbdd.crear_bbdd()

# Insertar datos de manera interactiva
bbdd.inserta_datos()
Este código proporciona una interfaz más estructurada utilizando la clase Bbdd para manipular bases de datos SQLite de manera eficiente. Además, permite a los usuarios definir la estructura de la base de datos y realizar operaciones de inserción según sus necesidades específicas.

python
Copy code
if __name__ == "__main__":
    # Solicitar el nombre de la tabla y generar el diccionario de columnas
    nombre_tabla = input('Introduce nombre de la tabla: ')
    diccionario_columnas = bbdd.crea_diccionario_columnas()

    # Crear la tabla en la base de datos
    bbdd.crear_bbdd(nombre_tabla, diccionario_columnas)

    # Solicitar la inserción de datos en la tabla creada
    insert = input('¿Quieres introducir datos en la tabla creada? ')
    if insert.lower() == 'si':
        while True:
            bbdd.inserta_datos(nombre_tabla, diccionario_columnas)
            seguir = input('¿Quieres introducir más datos (si/no): ')
            if seguir.lower() != 'si':
                break
Ahora, puedes utilizar la clase Bbdd para simplificar y estructurar tus operaciones con bases de datos SQLite en el contexto de tu biblioteca.
