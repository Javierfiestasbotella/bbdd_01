# Biblioteca de Manipulación de Bases de Datos SQLite en Python

Este código en Python proporciona una herramienta simple y efectiva para crear y gestionar bases de datos SQLite. Está especialmente diseñada para su uso en el contexto de una biblioteca, permitiendo a los usuarios definir tablas personalizadas con columnas específicas y luego insertar datos de manera interactiva.

## Características

- **Creación de Tablas Dinámicas:** La biblioteca ofrece una interfaz para crear tablas dinámicamente en una base de datos SQLite. Los usuarios pueden definir el nombre de la tabla y las columnas, junto con sus tipos de datos.

- **Generación de Diccionarios de Columnas:** Proporciona una función para generar diccionarios de columnas de manera interactiva, permitiendo a los usuarios especificar la cantidad de columnas y definir sus nombres y tipos de datos.

- **Inserción de Datos Interactiva:** La función de inserción de datos permite a los usuarios insertar datos en la tabla creada de manera interactiva, solicitando valores para cada columna.

## Ejemplo de Uso con la Clase `Bbdd`

```python
from bbdd import Bbdd

# Instanciar la clase
bbdd = Bbdd()

# Crear la base de datos y la tabla
bbdd.crear_bbdd()

# Insertar datos de manera interactiva
bbdd.inserta_datos()


¡Claro! Aquí tienes una versión mejorada y más legible de tu README:

markdown
Copy code
# Biblioteca de Manipulación de Bases de Datos SQLite en Python

Este código en Python proporciona una herramienta simple y efectiva para crear y gestionar bases de datos SQLite. Está especialmente diseñada para su uso en el contexto de una biblioteca, permitiendo a los usuarios definir tablas personalizadas con columnas específicas y luego insertar datos de manera interactiva.

## Características

- **Creación de Tablas Dinámicas:** La biblioteca ofrece una interfaz para crear tablas dinámicamente en una base de datos SQLite. Los usuarios pueden definir el nombre de la tabla y las columnas, junto con sus tipos de datos.

- **Generación de Diccionarios de Columnas:** Proporciona una función para generar diccionarios de columnas de manera interactiva, permitiendo a los usuarios especificar la cantidad de columnas y definir sus nombres y tipos de datos.

- **Inserción de Datos Interactiva:** La función de inserción de datos permite a los usuarios insertar datos en la tabla creada de manera interactiva, solicitando valores para cada columna.

## Ejemplo de Uso con la Clase `Bbdd`

```python
from bbdd import Bbdd

# Instanciar la clase
bbdd = Bbdd()

# Crear la base de datos y la tabla
bbdd.crear_bbdd()

# Insertar datos de manera interactiva
bbdd.inserta_datos()
Este código proporciona una interfaz estructurada utilizando la clase Bbdd para manipular bases de datos SQLite de manera eficiente. Permite a los usuarios definir la estructura de la base de datos y realizar operaciones de inserción según sus necesidades específicas.

Ejemplo de Uso Completo
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
Este ejemplo completo guía a los usuarios desde la creación de la base de datos y la tabla hasta la inserción de datos, proporcionando un escenario más realista y completo de cómo utilizar la biblioteca.

Instalación
Requisitos:

Python 3.x
SQLite3
Para instalar la biblioteca, utiliza el siguiente comando:
pip install tu-biblioteca
¡Bienvenido a simplificar tu manipulación de bases de datos SQLite con esta biblioteca en Python! ¡Esperamos que encuentres útiles estas herramientas!

Asegúrate de reemplazar `"tu-biblioteca"` con el nombre real de tu biblioteca. Este README proporciona una estructura más clara, destaca las características clave y brinda ejemplos de uso completo para hacerlo más atractivo y legible para los usuarios.

