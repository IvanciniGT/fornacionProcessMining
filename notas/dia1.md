
# Process Mining

## Procesos

Procesos de **negocio**:
Conjunto de tareas/actividades que realizamos en una empresa.. habitualmente siguiendo un determinado flujo de trabajo. Esos procesos buscan conseguir un objetivo de negocio.

**Negocio**: Debo conseguir llegar a ese objetivo al menor coste posible.. en todas las dimensiones: tiempo, recursos, dinero, etc.

Nuestro objetivo es **mejorar** esos procesos de negocio.

Cómo lo hacemos?
    - Conocer el proceso de negocio... Que no siempre es conocido. Muchas organizaciones... casi todas, tiene todos sus procesos documentados en Instrucciones técnicas, Manuales técnicos, Procedimientos, etc. Para según que certificaciones de Calidad nos hace falta tenerlo muy detallado, controlado...
   
    El papel lo aguanta todo.. y una cosa es cómo pone en los papeles que debemos realizar las tareas y otra cómo se realizan en la práctica.

    Hace 25 años an daba yo ayudando a empresas a informatizar (controlar/definir/automatizar) sus procesos de negocio. Esto surgió de la implantación de la norma ISO 9000, que obligaba a las empresas a definir sus procesos de negocio y a documentarlos. Esto es el primer paso. De alguna forma, al crear programas, se fuerza el seguir ciertos flujos de trabajo, pero no siempre se sigue el flujo de trabajo que se ha definido en los papeles. Y aún así... en muchas ocasiones, esos flujos eran demasiado abiertos.

    Necesitamos muchos datos. DATOS REALES de lo que ocurre.
    Esos datos contendrán EVENTOS generados por sistemas informáticos, que analizaremos para descubrir el proceso real que se está llevando a cabo. 
    Una parte del análisis será bastante evidente. Otra parte del análisis ya no será tan evidente...

## Minería

- Trabajo en una mina.. laboreo de minas...
- Criptomonedas
- **Data mining**

El process mining no es sino técnicas de minería de datos aplicadas a procesos de negocio.

Lo que se trata es de identificar patrones, relaciones, tendencias, etc. en los datos de eventos que se han generado en un proceso de negocio.

Gracias a esos patrones, relaciones, tendencias, etc. podemos:
- Descubrir cómo se está llevando a cabo un proceso de negocio
- Cómo se podría mejorar.
- Predecir dónde me va a dar problemas 

Adicionalmente, dentro de la Minería de procesos, agrupamos también técnicas básicas de análisis de datos, (Estadística nivel instituto) que nos ayuden con ciertas identificaciones en el mundo de los procesos de negocio.

Tenemos 2 partes conceptuales:
- Aplicar técnicas básicas estadísticas para analizar datos de eventos y entender cómo se comporta un proceso de negocio.
- Aplicar técnicas de minería de datos para descubrir patrones y relaciones en los datos de eventos, que me ayudan mucho más a entender cómo se comporta un proceso de negocio y cómo se podría mejorar.


---

# Recolección de datos

En el mundo del process mining, la recolección de datos está muy estandarizada. No hablamos de cualquier tipo de datos... hablamos de datos de eventos generados por sistemas informáticos que registran la ejecución de un proceso de negocio.

Esto implica, que sé/conozco/están estudiados y definidos los datos que necesito recoger para poder analizar un proceso de negocio:
- ID de una ejecución de un proceso de negocio (ID del caso)
- Cuando ocurre un evento (timestamp)
- Qué evento ocurre (nombre del evento)
Eso es el mínimo. Cualquier librería que nos permita realizar process mining, nos va a pedir esos 3 datos como mínimo.
Además de esos:
- Quién (humano o programa) ha generado en última instancia el evento (ID del recurso)
- Coste que tiene asociada la tarea (hora/hombre, dinero, etc.)
- etc.

No sólo están muy estudiados los datos que necesitamos recoger, sino que además, existen formatos muy estandarizados para almacenar esos datos de eventos. Los más conocidos son:
- **XES**: Extensible Event Stream. Es un formato XML que permite almacenar los datos de eventos de un proceso de negocio.
- Muchas veces usamos CSV, que es un formato muy sencillo y fácil de usar, pero no es tan rico como el XES.
- JSON
  
# Análisis de datos

Nos pasa lo mismo... En todo proceso de negocio busco lo mismo:
- Describir el proceso de negocio: Etapas, tareas, recursos, tiempos, costes, etc.
- Analizar el proceso de negocio: Identificar cuellos de botella, ineficiencias, etc.
- Mejorar el proceso de negocio: Proponer cambios, optimizaciones, etc.

En estos días, lo que vamos a hacer es:
- Entender los conjuntos de datos que vamos a analizar (qué campos tienen, qué significan, etc.)
- Entender qué formato se usan para representar esos conjuntos de datos (CSV, XES, JSON, etc.)
- Entender qué tipo de análisis podemos hacer con esos conjuntos de datos (estadística descriptiva, inferencial, data mining):
  - Discovery: Descubrimiento de procesos a partir de los datos de eventos.
  - Conformance: Conformidad de los procesos a partir de los datos de eventos.
  - Enhancement: Mejora de los procesos a partir de los datos de eventos.
- Aprender a usar una librería en python para analizar esos conjuntos de datos (pandas, pm4py, etc.)

## Pandas 

Es una librería genérica para el manipulación/análisis de datos en python. Muy inspirada en MATLAB.
Es cómoda.

## PM4Py

Es una librería específica para el análisis de datos de eventos de procesos de negocio. Está muy enfocada al process mining. LLeva incorporadas muchas técnicas de minería de datos y análisis de datos muy específicas que aplicamos a los datos de eventos de procesos de negocio.


# Cómo enfrentarnos a un trabajo de process mining

1º Extraer datos
2º Manipular los datos **CRITICO** <<< Pandas
2.5º Guardar los datos preparados para su uso futuro.
3º Analizar los datos  <<< Pandas + PM4Py
4º Visualizar los datos 


Todo esto.. son proyectos donde no hay un final. 
Podré mejorar algo un proceso... y esa mejora impactará en el proceso de negocio, y eso generará nuevos datos de eventos, que podré analizar para ver si la mejora ha sido efectiva o no... o si ha generado nuevos cuellos de botella, ineficiencias, etc.

Todos estos estudios son estudios VIVOS en el tiempo.
Querré reaprovechar datos de eventos de procesos de negocio que ya he analizado en el pasado, y que me pueden ayudar a analizar nuevos datos de eventos de procesos de negocio.
---


IAs???

Con inteligencia artificial nos referimos a cualquier máquina o programa que simula un compartamiento inteligente. 

Estos programas tradicionalmente los hemos creado de 2 formas diferentes:
1. **Programación basada en reglas**: Definimos un conjunto de reglas que el programa debe seguir para tomar decisiones. Estas reglas son escritas por humanos y pueden ser muy específicas o generales.
2. **Aprendizaje automático (Machine Learning)**

## Machine Learning

Son técnicas que nos ayudan a generar modelos (programa), que simula un comportamiento inteligente. Esos programas pueden ayudarnos a:
- Clasificar datos
- Predecir datos
- Agrupar datos
- Generar datos nuevos <--- Revolución de los últimos años. IAs Generativas

Lo curioso es que estos programas no los escribimos los humanos. Son demasiado complejos... Nuestro limitado cerebro (limitado a la hora de retener/procesar datos) no es capaz de escribir un programa que simulen ciertos comportamientos:
- Reconocer/leer una matricula en una fotografía. Los humanos no tenemos NPI de cómo hacer ese programa.
- Traducir un texto a un lenguaje.
- Leer un texto (voz)

Qué hacemos... pedir a la computadora que haga ese programa (modelo). La computadora para ello, lo que necesita es una gran cantidad de datos. Y la computado no entiende el problema que está resolviendo... solamente echa cuentas y busca una ecuación matemática que maximice la probabilidad de acertar (cometer pocos errores) en la resolución de un problema para el conjunto de datos que le hemos proporcionado.

Esto es complicado.. De hecho es tan complicado, que ni siquiera cuando la computadora crea ese programa, y me da el programa, yo soy capaz de entender cómo funciona ese programa. Es un programa que no he escrito yo, y que no entiendo. Pero funciona.

## Data mining

Es un previo al machine learning. Es un proceso de análisis de datos.


## Análisis de datos

Desde hace milenios la humanidad está analizando conjuntos de datos.
Las técnicas más básicas tienen más de 2000 años... y son estudiadas por la ESTADÍSTICA.

La estadística es una ciencia que estudia la recogida, análisis, interpretación, presentación y organización de conjuntos de datos.
Las técnicas más básicas, que son las que estudiamos a nivel de instituto: Técnicas DESCRIPTIVA.

Hay técnicas mucho más avanzadas: ESTADISTICA INFERENCIAL, que nos permite introducirnos en el mundo de las predicciones (al más puro estilo Rapel, con una bola de cristal.. o leyendo los posos del café).
La única gracia es que la estadística inferencial me ofrece la posibilidad de tasar la probabilidad de que equivocarme.

BANCO €€€. Me importa acertar al conceder a una persona una hipoteca pensando en que si me va a pagar? NO
Lo único que le importar es saber en qué % de casos se va a equivocar!!!

Todo esto de la estadística funciona bien cuando tengo 1, 2... 3 se me hace ya complicado. El cerebro no nos da de si. Hacer un análisis donde tengamos más de 3 variables... somos INCAPACES.
De entrada hay muy pocos gráficos donde podamos representar cómodamente 3 variables.

En un momento dado, aparecen algoritmos en el mundo de las ciencias de la computación que nos permiten analizar grandes cantidades de datos, y que nos permiten analizar más de 3 variables.
Esos algoritmos juntos con la aplicación de esas técnicas de estadística son los que dan lugar a lo que conocemos como **Data Mining** y **Machine learning**
- Técnicas de clustering
- Análisis de series temporales
- Redes neuronales

## Data Mining

Es cuando le pido a la computadora que analice un conjunto de datos y me encuentre patrones, relaciones, tendencias, etc. en esos datos, cuando tengo más de 3/4 variables en el conjunto de datos.
Yo humano soy incapaz... mi limitado cerebro no da de si. Pero la computadora si.
No sé que busco... solo sé que quiero buscar algo. Igual que en el mundo del laboreo de minas, donde el minero no sabe que va a encontrar, Solo sé que me pongo caso, pico, pala y a cavar... a ver que encuentro, si es que encuentro algo.




---

# Instalar pandas.

Cuando para un proyecto necesitamos una librería, la instalamos...
Eso lo hemos:

$ python -m pip install PAQUETE
$ python -m pip install pyyaml

Antiguamente:

$ pip install PAQUETE # Desuso

Una cosa que no conté...
Cuando trabajamos en varios proyectos, cada proyecto puede necesitar una versión diferente de una librería.
O que un proyecto necesite una librería y ésa a su vez necesite otra librería... de una versión concreta, y diferente de otra versión que necesita otro proyecto.

Para resolver esto, cada vez que creamos un proyecto creamos un entorno virtual. Un entorno virtual es un espacio aislado donde podemos instalar las librerías que necesitemos para ese proyecto, sin interferir con otros proyectos.

 python -m venv venv

Para activar ese entorno: 
- Mac/Linux: source venv/bin/activate
- Windows: venv\Scripts\activate

Una vez ejecutado eso, las librerías que instalemos se instalarán en ese entorno virtual, y no afectarán a otros proyectos.

IMPORTANTISIMO: Cada vez que vaya a ejecutar el proyecto: 
- Activar el entorno virtual:
    - Mac/Linux: source venv/bin/activate
    - Windows: venv\Scripts\activate

Si en windows, no os deja ejecutar lo del activate:
- En el icono de windows buscamos "powershell" y lo ejecutamos como administrador.
- Y dentro ejecuto :
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Para instalar ahora, dentro del entorno virtual, la librería pandas, ejecutamos:

```bash
python -m pip install pandas
```


---

# Estadísticos básicos:

La estadística nos ayuda a entender un conjunto de datos.
El tener datos no significa que los entendamos.

De cara a entender los datos, lo que voy es resumiéndolos... A eso me ayuda la estadística:
1. Tabla de frecuencias

    Rangos de salario:      #personas   %personas
     0-1000:                    5       1%
     1000-2000:                10       2%
     2000-3000:                15       3%
     3000-4000:               200      10%
     4000-5000:              5000      79%

2. Pintar esas tablas de frecuencia: Un gráfico de barras, un diagrama de sectores (tarta)

Pero la estadística me da más herramientas, que me permiten resumir aún más los datos:
1º Medidas de tendencia central: Me informan de POR DONDE VAN LOS TIROS!
    Moda:     Valor que más se repite en un conjunto de datos (el de mayor frecuencia): 4000-5000
    Mediana:  Valor de la variable que divide en 2 partes iguales(o los más iguales posible.. en cantidad) un conjunto de datos ordenados.                                                      4000-5000
    Media:    Es el más raro.. y el más difícil de entender. No atienda a conceptos humanos...
              Es una fórmula matemática que nos da un valor que representa el conjunto de datos.
              Suma todos y divide entre el número de datos.
              Es el más utilizado en el mundo de la estadística, pero es el que menos sentido práctico tiene.
              Y nos equivocamos mucho muchísimo al interpretarlo.                       4000-5000

    En muchas ocasiones, la media no es representativa del conjunto de datos.

    Cualquier unidad de tendencia central por si sola no vale de nada.
    NUNCA JAMAS en un informe, en un estudio puedo usar una unidad de tendencia central sin ofrecer su medida de dispersión asociada.
2º Medidas de dispersión: Me informan de COMO CAMBIAN LOS DATOS CON RESPECTO AL POR DONDE VAN LOS TIROS.

Estoy en una calle... donde hay muchos portales de viviendas.
Portal 1: 4 personas, de las que mido sus alturas: 

    160cm , 170cm, 180cm, 190cm ---> MEDIA:    175cm 
                                     MEDIANA:  175cm

Portal 2: 4 personas, de las que mido sus alturas:

    160cm , 160cm, 190cm, 190cm ---> MEDIA:    175cm
                                     MEDIANA:  175cm

Portal 3: 4 personas, de las que mido sus alturas:

    175cm , 175cm, 175cm, 175cm ---> MEDIA:    175cm
                                     MEDIANA:  175cm

Portal 4: 4 personas, de las que mido sus alturas:

   150cm , 160cm, 190cm, 200cm --->  MEDIA:    175cm
                                     MEDIANA:  175cm

Tengo 4 portales TOTALMENTE DIFERENTES ENTRE SI, pero todos tienen la misma media y mediana.