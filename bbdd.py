import sqlite3
class Bbdd:
    def __init__(self, nombre_bbdd='',nombre_tabla='',columnas={}):
        self.nombre_bbdd = nombre_bbdd
        self.nombre_tabla = nombre_tabla
        self.columnas = columnas
        print('Se ha creado el inicio de una bbdd')
    
    
    def crear_bbdd(self):
        try:
            if self.nombre_bbdd == '':
                self.nombre_bbdd = input('Introduce el nombre de la bbdd: ')
                self.nombre_bbdd += '.db'
                self.nombre_tabla = input('Introduce nombre de la tabla: ')
            else:
                print('Ya existe una base de datos con este nombre')

            self.columnas = self.crea_diccionario_columnas()
            self.mi_conexion = sqlite3.connect(self.nombre_bbdd)
            self.mi_cursor = self.mi_conexion.cursor()

            # Construir la parte de la consulta SQL para las columnas
            self.columnas_sql = ', '.join([f'{key} {value}' for key, value in self.columnas.items()])

            # Crear la tabla
            self.mi_cursor.execute(f'''
                CREATE TABLE {self.nombre_tabla} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    {self.columnas_sql}
                )
            ''')

            self.mi_conexion.commit()

        except sqlite3.Error as e:
            print(f"Error al conectar o ejecutar la consulta: {e}")

        finally:
            # Cerrar la conexión, independientemente de si hubo un error o no
            if 'mi_conexion' in locals():
                self.mi_conexion.close()
    
        
    def menu(self):
        print ( '''
        1- Crear Base de Datos
        2- Insertar datos en bbddd
        3- Salir
        ''')
        
    def start(self):
        while True:
            self.menu()
            quest= int(input('Introduce una opción: '))
            if quest == 1:
                self.crear_bbdd()
            elif quest == 2:
                while True:
                    self.inserta_datos()
                    self.seguir = input('Quieres introducir más datos (si/no): ')
                    if self.seguir.lower() != 'si':
                        break
            elif quest == 3:
                break
            else:
                print('Has introducido un valor erróneo.')
            
    def crea_diccionario_columnas(self):
        while True:
            try:
                self.cantidad_elementos = int(input('Introduce la cantidad de elementos: '))
                if self.cantidad_elementos >= 0:  # Verifica que la cantidad sea un número no negativo
                    break
                else:
                    print('Error: Ingresa un número entero no negativo para la cantidad de elementos.')
            except ValueError:
                print('Error: Ingresa un número entero para la cantidad de elementos.')

        for _ in range(self.cantidad_elementos):
            while True:
                try:
                    self.nombre_columna = input('Introduce el nombre de la columna: ')
                    self.tipo_columna = input(f'Introduce el tipo de la columna {self.nombre_columna} (por ejemplo, VARCHAR, INTEGER): ')
                    self.columnas[self.nombre_columna] = self.tipo_columna
                    break
                except ValueError:
                    print('Error: Ingresa un tipo de dato válido para la columna.')

        return self.columnas



    def averiguar_campos(self):
        try:
            # Conectar a la base de datos SQLite
            self.conn = sqlite3.connect(self.nombre_bbdd)
            self.cursor = self.conn.cursor()
            self.dic = {}

            # Obtener los nombres de los campos de una tabla
            self.tabla = self.nombre_tabla
            self.cursor.execute(f"PRAGMA table_info({self.tabla})")
            self.campos = self.cursor.fetchall()

            # Imprimir los nombres de los campos
            for campo in self.campos[1:]:
                self.dic[campo[1]] = campo[2]

            # Cerrar la conexión
            self.conn.close()

            return self.dic

        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            self.menu()

        except sqlite3.OperationalError as e:
            print(f"Error al ejecutar la consulta: {e}")
            self.menu()

    
    
       
    def inserta_datos(self):
        if self.nombre_bbdd == '' and self.nombre_tabla == '':
            self.nombre_bbdd = input('Introduce el nombre de la bbdd: ')
            self.nombre_bbdd += '.db'
            self.nombre_tabla = input('Introduce nombre de la tabla: ')
        self.columnas=self.averiguar_campos()
        self.mi_conexion = sqlite3.connect(self.nombre_bbdd)
        self.mi_cursor = self.mi_conexion.cursor()

        self.valores = tuple(input(f'Introduce {key}: ') for key in self.columnas.keys())
        self.mi_cursor.execute(f'INSERT INTO {self.nombre_tabla} VALUES (NULL, {", ".join(["?"] * len(self.columnas))})', self.valores)

        self.mi_conexion.commit()
        self.mi_conexion.close()

        
if __name__ == "__main__":
    bbdd_001=Bbdd()
    bbdd_002=Bbdd()
    bbdd_002.start()
     
