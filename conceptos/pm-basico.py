import pandas as pd     # Manipular datos

# Ayer usamos pandas para crear un conjunto de datos... programáticamente.
# Hoy lo tengo... en un fichero CSV (EXCEL). También nos ayuda a cargarlo.

#datos = pd.read_csv('datos.csv')  # Cargar el fichero CSV
#print(datos) # Ya veo los datos. Se han cargado bien? A priori las fechas se han tomado como textos
#print(datos.info())

datos = pd.read_csv('datos.csv', parse_dates=['timestamp'])  # Cargar el fichero CSV y parsear la columna Fecha como fechas

#print(datos) # Ya veo los datos. Se han cargado bien? A priori las fechas se han tomado como textos
#print(datos.info())

# Puedo saber las tareas diferentes que se están ejecutando?
# Podría hacer una tabla de frecuencias la columna activity:
#print(datos['activity'].value_counts())  # Imprime el número de veces que aparece cada actividad en la columna activity
# Si solo quisiera ver las tareas:
#print(datos['activity'].unique())  # Imprime las tareas diferentes que se están ejecutando

# Cuánto tardan esas tareas?
# Qué tarea se ejecuta primero?
# Agrupa las tareas por su nombre de caso (case_id), ordena por fecha, y dame el nombre de la primera y la última tarea de cada caso, y el tiempo que ha tardado en ejecutarse cada una.
#tareas_ordenadas_por_caso_y_fecha= datos.sort_values(by=['case_id', 'timestamp'])  # Ordena los datos por case_id y timestamp
#print(tareas_ordenadas_por_caso_y_fecha)  # Muestra las tareas ordenadas por caso y fecha

# Agrupa las tareas por case_id y calcula el tiempo que ha tardado en ejecutarse cada una
#tareas_por_caso = tareas_ordenadas_por_caso_y_fecha.groupby('case_id').agg(
#    primera_tarea=('activity', 'first'),  # Toma la primera tarea del caso
#    ultima_tarea=('activity', 'last'),     # Toma la última tarea del caso
#)
#print(tareas_por_caso)  # Muestra las tareas agrupadas por caso
# Parece que el proceso empieza siempre por: "Pedido recibido"
# Parece que el proceso acaba siempre en "Aprobación" o en "Rechazo"
# Hay otras tareas "Validación"
# Vamos a usar pm4py para todo esto.
# Aunque a pm4py le tengo que dar la tabla con unos nombres de columnas muy particulares.

datos_renombrados = datos.rename(columns={
    'case_id': 'case:concept:name',
    'activity': 'concept:name',
    'timestamp': 'time:timestamp'
})  # Renombra las columnas para que pm4py las entienda

# Estalibrería también espera que los datos lleguen ordenados por caso y por fecha
datos_renombrados = datos_renombrados.sort_values(by=['case:concept:name', 'time:timestamp'])  # Ordena los datos por case_id y timestamp
print(datos_renombrados)  # Muestra los datos renombrados

# Si quiero usar la librería pm4py, necesito instalarla y luego importarla
# python3 -m pip install pm4py # Pero esto necesito hacerlo en mi entorno virtual

from pm4py.objects.conversion.log import converter

# Una vez tenemos la librería, podemos empezar a usarla.
# Para ello, le pedimos que procese esos datos (eventos) que hemos cargado

log = converter.apply(datos_renombrados, variant = converter.Variants.TO_EVENT_LOG)  # Convierte los datos a un log de eventos de pm4py
print(log)  # Muestra el log de eventos

# Vamos a hacer DISCOVERY de procesos... queremos ver qué flujo de tareas se están ejecutando

from pm4py.algo.discovery.inductive import algorithm as inductive_miner
from pm4py.objects.conversion.process_tree import converter as process_tree_converter
petry = inductive_miner.apply(log)  # Aplica el algoritmo de descubrimiento inductivo a los datos
net, im, fm = process_tree_converter.apply(petry)  # Convierte el árbol de procesos a una red de Petri
print(petry)  # Muestra el árbol de procesos descubierto

print(net, im, fm)

from pm4py.visualization.petri_net import visualizer as pn_visualizer

gviz = pn_visualizer.apply(net, im, fm, parameters={"format": "png"})  # Visualiza la red de Petri resultante del descubrimiento
pn_visualizer.save(gviz, "proceso.png")  # Guarda la visualización en un fichero PNG

# falta graphviz
# Necesitamos instalar el programa graphviz
# Añadir la librería de python que permite hablar con ese programa
# python -m pip install graphviz

