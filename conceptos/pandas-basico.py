print("Introducción a pandas")

import pandas as pd   # TODO EL MUNDO LO HACE... Todo ejemplo que veas en internet importa pandas como pd


# Pandas nos ofrece un tipo de dato llamado DataFrame (Clase)
# Un dataframe es como una hoja de un libro Excel.
# Una tabla de datos, con filas y con columnas.

mi_dataframe = pd.DataFrame()
print(mi_dataframe) # Empty dataframne (una tabla vacía)

nombres = ("Federico", "Menchu", "Felipe")
mi_dataframe = pd.DataFrame(nombres)
print(mi_dataframe) # Un dataframe con 1 columna y 3 filas

# Podemos dar nombres a las columnas, al crear un dataframe     
mi_dataframe = pd.DataFrame(nombres, columns=["Nombre"])
print(mi_dataframe) # Un dataframe con 1 columna y 3 filas, con el nombre de la columna

# 1 columna... es muy cutre... queremos más columnas
personas = ( ("Federico", 30, "Madrid"),
            ("Menchu", 28, "Barcelona"),
            ("Felipe", 25, "Valencia") )
mi_dataframe = pd.DataFrame(personas, columns=["Nombre", "Edad", "Ciudad"])
print(mi_dataframe) # Un dataframe con 3 columnas y 3 filas

# Me puede interesar solo tomar una columna de datos
print(mi_dataframe["Nombre"]) 
print(mi_dataframe["Edad"]) 

# Me puede interesar acceder a una fila

print(mi_dataframe.iloc[0])  # Accede a la primera fila (0 es el índice de la primera fila)
print(mi_dataframe.iloc[1])  # Accede a la segunda fila (1 es el índice de la segunda fila)

# Puedo querer también ir a una celda concreta
print(mi_dataframe.iloc[0]['Edad'])  # Accede a la celda de la primera fila y de ella a la columna Edad
print(mi_dataframe.iloc[2]['Ciudad'])  # Accede a la celda de la tercera fila y de ella a la columna Ciudad

# Esta es una formad e crear conjuntos de datos (tablas, dataframes) de forma manual.
# Hay más formas:

personas = { "Nombre": ("Federico", "Menchu", "Felipe"),
             "Edad": (30, 28, 25),
             "Ciudad": ("Madrid", "Barcelona", "Valencia") }
mi_dataframe = pd.DataFrame(personas) # En este caso no hace falta nombrar las columnas, ya que las claves del diccionario son los nombres de las columnas
print(mi_dataframe) # Un dataframe con 3 columnas y 3 filas

# Más adelante veremos como cargar datos desde ficheros: TXT, CSV, EXCEL...
# Eso nos interesará mucho... no queremos en la mayor parte de los casos crear dataframes a mano.
# A veces si.

# Lo que si.. es que si cargo un fichero con 50.000 filas... puede que no me interese que lo imprima entero en pantalla.
# Pero si me puede interesar imprimir algunas filas, las primeras, las últimas, o una muestra aleatoria.
print(mi_dataframe.head())  # Imprime las primeras 5 filas del dataframe
print(mi_dataframe.head(1))  # Imprime las primeras 10 filas del 

print(mi_dataframe.tail())  # Imprime las últimas 5 filas del dataframe
print(mi_dataframe.tail(2))  # Imprime las últimas 2 filas del dataframe

print(mi_dataframe.sample(2))  # Imprime 2 filas aleatorias del dataframe

# Saber el tamaño del dataframe (de la tabla de datos)
print(mi_dataframe.shape)  # Imprime una tupla con el número de filas y columnas del dataframe (3, 3)
# Saber el número de celdas
print(mi_dataframe.size)  # Imprime el número de celdas del dataframe (9, ya que hay 3 filas y 3 columnas)

# Cada columna tiene un tipo de dato asociado
# Puedo tener columnas con números enteros, con números decimales, con textos, con valores lógicos, con fechas...
# A veces me interesa saber el tipo de datos de cada columna.
# En muchos casos, por ejemplo, al cargar datos de un excel (CSV) las fechas se me reconocen como textos.
# Eso no nos vale para luego analizar los datos, ya que no podré hacer operaciones con ellas.
# En esos casos, tendremos que hacer conversiones de tipos de datos.
# Pero lo primero es saber el tipo de datos de cada columna.
print(mi_dataframe.dtypes)  # Imprime el tipo de dato de cada columna del dataframe
# Los textos se reconocen como object
# los números enteros como int64
# los números decimales como float64
# los valores lógicos como bool
# las fechas como datetime64[ns]

print(mi_dataframe.describe()) # De todas las columnas numéricas, me da un resumen estadístico

# Para 