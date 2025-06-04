
# Minería de procesos: Process Mining

Técnicas de Data mining para la mejora de procesos de negocio.
Aplicamos técnicas estadísticas básicas y también más avanzadas (del data mining) para conseguir:
- Discovery: Entender cómo se comporta el proceso en la realidad.
- Compliance: Verificar si el proceso se ajusta a lo establecido.
- Enhancement: Mejorar el proceso.

Flujo de trabajo para hacer process mining:
- Necesitamos datos... Nos vienen de sistemas informáticos:
  Entre esos datos, destacan 3:
  - Identificador de una instancia del proceso (ej. número de expediente).
  - Fecha en la que ocurre
  - Evento asociado a la instancia del proceso (ej. "Solicitud recibida", "Solicitud aprobada", "Solicitud denegada").
  - Duración (habitualmente la obtenemos de la diferencia con el evento anterior)
  - Coste (tiempo, dinero, recursos...)
  - Recurso
  Estos datos, decíamos que hay formatos que usamos habitualmente:
  - CSV
  - JSON
  - XML (hay un esquema XML especial para process mining, XES=eXtended Event Stream)
  Ciertos sistemas (SAP, ...) generan formato XES directamente.
  Otros no... y los sacamos como podemos.. y más curro en manipulación
- Los manipulo, pa' dejarlos niquela'os
- Guardarlos para su uso futuro
- Analizar los datos
- Visualizar los resultados y sacar conclusiones

En nuestro caso, vamos a estar haciendo process mining usando librerías de python.
Escribiremos programas para cada una de esas tareas .. de ahí arriba!

Librerías:
- Pandas
- PM4PY

---

# Estadística

Nos ayuda a entender una población (conjunto). El tener datos no implica que entienda lo que significan.
En Entender / Aprender es una cuestión de resumir y descartar información... (así lo hace el cerebro).

## Técnicas para resumir los datos

1. Tablas de frecuencia. Resumo la información mucho.
En lugar de tener 1000 nóminas, tengo una tabla con 8 rangos salariales... y el número de personas que están en cada rango (FRECUENCIA)
   - Tablas de frecuencias absolutas: número de personas en cada categoría.
   - Tablas de frecuencias relativas: porcentaje de personas en cada categoría.
   - Tablas de frecuencias acumuladas: número acumulado de personas hasta esa categoría.
   Esas tablas puedo representarlas gráficamente: diagrama de barras (absolutos) / sectores (relativos).
2. Podemos resumir aún más:
   Medidas de tendencia central: Saber por donde van los tiros! En torno a qué valor se agrupan los datos.
   - Moda: valor que más se repita
   - Mediana: valor que divide los casos en dos mitades, más o menos(50% de los datos están por debajo y 50% por encima).
   - Media: Es COMPLEJA porque atiende a una ecuación matemática.
      SUMO todos los valores y divido entre el número de valores.
   Medidas de dispersión: Saber cuanto cambian los datos con respecto al POR DONDE VAN LOS TIROS.

Proceso de gestión de expedientes. Y una de las tareas que hay que hacer es APROBARLO.
Y mido los tiempos que se tarda en aprobar los expedientes del último año.

1 2 1 4 8 6 2 3 1 2 5 2 3 2 4 1 7 2 9 2 3 1 4 2 1 3 6 1 2 1 4 8 6 2 3 1 2 5 2 3 2 4 1 7 2 9 2 3 1 4 2 1 3 6 1 2 1 4 8 6 2 3 1 2 5 2 3 2 4 1 7 2 9 2 3 1 4 2 1 3 6 1 2 1 4 8 6 2 3 1 2 5 2 3 2 4 1 7 2 9 2 3 1 4 2 1 3 6 1 2 1 4 8 6 2 3 1 2 5 2 3 2 4 1 7 2 9 2 3 1 4 2 1 3 6 1 2 1 4 8 6 2 3 1 2 5 2 3 2 4 1 7 2 9 2 3 1 4 2 1 3 6 1 2 1 4 8 6 2 3 1 2 5 2 3 2 4 1 7 2 9 2 3 1 4 2 1 3 6 1 2 1 4 8 6 2 3 1 2 5 2 3 2 4 1 7 2 9 2 3 1 4 2 1 3 6 1 2 1 4 8 6 2 3 1 2 5 2 3 2 4 1 7 2 9 2 3 1 4 2 1 3 6 1 2 1 4 8 6 2 3 1 2 5 2 3 2 4 1 7 2 9 2 3 1 4 2 1 3 6 1 2 1 4 8 6 2 3 1 2 5 2 3 2 4 1 7 2 9 2 3 1 4 2 1 3 6 1 2 1 4 8 6 2 3 1 2 5 2 3 2 4 1 7 2 9 2 3 1 4 2 1 3 6 1 2 1 4 8 6 2 3 1 2 5 2 3 2 4 1 7 2 9 2 3 1 4 2 1 3 6 1 2 1 4 8 6 2 3 1 2 5 2 3 2 4 1 7 2 9 2 3 1 4 2 1 3 6 1 2 1 4 8 6 2 3 1 2 5 2 3 2 4 1 7 2 9 2 3 1 4 2 1 3 6 1 2 1 4 8 6 2 3 1 2 5 2 3 2 4 1 7 2 9 2 3 1 4 2 1 3 6 1 2 1 4 8 6 2 3 1 2 5 2 3 2 4 1 7 2 9 2 3 1 4 2 1 3 6 1 2 1 4 8 6 2 3 1 2 5 2 3 2 4 1 7 2 9 2 3 1 4 2 1 3 6 1 2 1 4 8 6 2 3 1 2 5 2 3 2 4 1 7 2 9 2 3 1 4 2 1 3 6  ... 1000 datos

    TABLA DE FRECUENCIAS:

                          FREQUENCIA ABSOLUTA       FREQ RELATIVA       FREQ ACUMULADA
       Tiempo              Cuantos expedientes          %                   %A
        1                    100                    100/650 = 15.38%        15.38%
        2                    300                    300/650 = 46.15%        61.54%
        3                    180                    180/650 = 27.69%        89.23%
        4                     35                    35/650 =  5.38%         94.62%
        5                     25                    25/650 =  3.85%         98.46%
        +6                    10                    10/650 = 1.54%         100.00%
                        ----------
                             650
    MODA                2
    MEDIANA             2
    MEDIA               1*100+2*300+3*180+4*35+5*25+6*10 / 650 = 2.15


## Cálculo de la mediana:
    
    1 2 3 4 6 3 2 5 <--- MEDIANA ES 3

    1º Ordenar los datos:    1 2 2 3     3 4 5 6
    2º Si el número de datos es impar, la mediana es el valor del medio.
       Si es par, la mediana es la media de los dos valores del medio.
       En nuestro caso, 8 datos = PAR, así que la mediana es la media de los dos valores del medio:
       (3 + 3)/2 = 3
     En este caso, si tomo los datos menores o iguales a 3, tengo   1 2 2 3 3   50%? NO  5/8= 62.5%
     Y los mayores o iguales a 3, tengo                             4 5 6       50%? NO  3/8= 37.5%

     Y es lo mejor que puedo hacer.. no hay criterio alguno para separar esos datos en 2 grupos de tamaño más similar entre si, atendiendo únicamente al valor de la variable.
                                       GRUPO A     GRUPO B
     Si hubiera cortado en el 1:          1           7
     Si hubiera cortado en el 2:          3           5
     Si hubiera cortado en el 3:          5           3 *****
     Si hubiera cortado en el 4:          6           2
     Si hubiera cortado en el 5:          7           1

# Cuál nos interesa para trabajar?

Moda, mediana o media?
Depende.... del caso... Pero... debe haber alguna regla.

Cuál es el objetivo? Entender los datos.
Necesito un dato que cuando lo lea o escuche, me ayude a entender mejor los datos... y no me genere confusión.

## Sease villa-arriba de arriba

Tiene 10 vecinos... con sus coches... que contaminan al día:

 5gCO/Dia 5 5 10 10 10 10 15 15 15

 De media cuánto contaminan en VA-A? 10gCO/día
 De mediana cuánto contaminan en VA-A? 10gCO/día

   ^
   |     X
   |  X  X  X
   |  X  X  X
   |  X  X  X
   +-------------> Contaminación
      5 10  15
        ^
        MEDIANA
        MEDIA

## Sease villa-abajo de abajo

Tiene 10 vecinos... con sus coches... que contaminan al día:
Muy mentalizados ellos.. Se han ido después de 10 juntas de vecinos.. que se han puesto de acuerdo en comprar todos el mismo coche eléctrico para contaminar menos...  Les han hecho precio

 5gCO/Dia 5 5 5 5 5 5 5 5 1000

 De mediana cuánto contaminan en VA-B? 5gCO/día
 De media cuánto contaminan en VA-B?   1000+9*5 = 1045/10 = 104.5gCO/día

                                            ^  x
                                            |  X
                                            |  X
                                            |  X
                                            |  X                                               x
<-------------------------------------------+-------------------------------------------------------> CONTAMINACION
    GERTRU                                     5                     104,5                   1000
                                               ^                                              MANOLO
                                            MEDIANA
                                 <-----------MEDIA----------------->

Si miro a la media, me da una idea de que en VA-Abajo están muy sensibilizados con el medio ambiente... o no? Me llevo a la idea de que los coches en general en VA-Abajo son muy contaminantes... mucho más que en VA-arriba. Y es cierto? Nada más lejos de la realidad.

La media es lo que en estadística llamamos un indicador SUFICIENTE, su cálculo tiene en cuenta TODOS LOS DATOS... Pero también es lo que llamamos un indicador NO ROBUSTO, se ve muy afectada por datos extremos... como MANOLO.

Por contra la MEDIANA es un indicador ROBUSTO, porque no se ve afectada por los datos extremos, y es un indicador NO SUFICIENTE, porque no tiene en cuenta todos los datos, solo algunos.

En general preferimos la MEDIA... pero hay veces que no es representativa del colectivo. SI ES REAL.. pero no es un buen resumen de la realidad.

En qué me baso para determinar si la media es un buen resumen de la realidad?, o si por el contrario debo elegir la mediana? EN LA FORMA (ASIMETRIA) DE LA DISTRIBUCIÓN DE LOS DATOS.

La media siempre quiere estar con la mediana... pero los datos extremos tiran de ella

- En distribuciones simétricas, la media es igual a la mediana... y en este caso, la media es un buen resumen de la realidad.
- En distribuciones asimétricas, la media se desplaza hacia el lado de los datos extremos, y la mediana es un mejor resumen de la realidad
  
En muchos casos, simplemente calculamos las 2... y si difieren mucho, nos quedamos con la mediana. (MAS PRACTICO)

Qué es mucho? o POCO? Sentido común aplicado al negocio.

                        APROBAR EXPEDIENTES      PREPARAR EXPEDIENTE
Media de tiempo en:          2,56 horas                20 horas
Mediana de tiempo en:        2,30 horas                16 horas


En la realidad, los datos que no están manipulados por el ser humano (donde el ser humano interviene poco)... tienden a la simetría.
Altura de la gente.    SIMETRICA
Peso de la gente.      ASIMETRICA
SALARIO DE LA GENTE    ASIMETRICA


Por ejemplo, ésto será crítico al analizar los procesos de negocio.. y los tiempos que tarda cada actividad en realizarse.
Tendré muchos datos... pero no los entiendo.. y tengo que empezar a resumirlos para entenderlos mejor.


- Podré encontrarme con tareas de un proceso de negocio que siempre duren lo mismo, con independencia del caso concreto
   Dar de alta un expediente: Se tarda 1 hora. Tanto Felipe, como Menchu, como Federico... todos tardan una hora.
   Qué me interesa, media o mediana? NINGUNO.. Ese tiempo es CONSTANTE! y a las constantes no se les aplican técnicas de estadística.

   En aprobar ese expediente tardemos entre 1 hora y 20 hora (MIN, MAX: Estadísticos de posición)
   La media es 15 y la mediana es 10.
   Es muy asímetrico... Lo que tenemos es unos cuantos expedientes (MANOLOS) que tardan mucho más que el resto y suben la media.
   Además hay otro concepto ... los datos muestran mucha VARIEDAD... son muy diferentes entre si.
   Habrá receta mágica para mejorar esta tarea? Una receta de café para todos? NO.
   Posiblemente tenga que comenzar a analizar los expedientes que más tardan... ver que tienen en común... y ver si puedo hacer algo para que esos expedientes no tarden tanto.

   Distinto será una tarea como el alta... que es el extremo opuesto... Todos los datos iguales. Y puedo optimizar esa tarea de forma que todas las altas tarden la mitad.


# Ayer comenté que la media o mediana no son suficientes para entender los datos.

Siempre debo dar una medida de dispersión


    Estoy en una calle... donde hay muchos portales de viviendas.
    Portal 1: 4 personas, de las que mido sus alturas: 

        160cm , 170cm, 180cm, 190cm ---> MEDIA:    175cm 
                                         MEDIANA:  175cm

         -15     -5     5      15        MEDIA DESVIACIONES:  0
          15      5     5      15        MEDIA ABS DESVIACIONES:  10
          225     25    25     225       MEDIA CUADRADO DE LAS DESV: 500/4 = 125
                                         RAIZ MEDIA DEL CUADRADO DE LAS DESVIACIONES: 11.18cm (DESVIACIÓN TÍPICA)

    Portal andén 3/8
        165cm , 165cm, 185cm, 185cm ---> MEDIA:    175cm 
                                         MEDIANA:  175cm

         -10     -10     10     10       MEDIA DESVIACIONES:  0
          10      10     10     10       MEDIA ABS DESVIACIONES:  10 (2 poblaciones diferentes pueden dar la misma desv. media)
         100     100    100    100       MEDIA CUADRADO DE LAS DESV: 400/4 = 100
                                         RAIZ MEDIA DEL CUADRADO DE LAS DESVIACIONES: 10cm (DESVIACIÓN TÍPICA)

    Portal 2: 4 personas, de las que mido sus alturas:

        160cm , 160cm, 190cm, 190cm ---> MEDIA:    175cm
                                         MEDIANA:  175cm

         -15     -15    15     15        MEDIA DESVIACIONES:  0
          15      15    15     15        MEDIA ABS DESVIACIONES:  15
         225     225    225    225       MEDIA CUADRADO DE LAS DESV: 900/ 4 = 225
                                         RAIZ MEDIA DEL CUADRADO DE LAS DESVIACIONES: 15cm (DESVIACIÓN TÍPICA)

    Portal 3: 4 personas, de las que mido sus alturas:

        175cm , 175cm, 175cm, 175cm ---> MEDIA:    175cm
                                         MEDIANA:  175cm

         0       0     0       0        MEDIA DESVIACIONES:  0
         0       0     0       0        MEDIA ABS DESVIACIONES:  0
         0       0     0       0        MEDIA CUADRADO DE LAS DESV: 0
                                        RAIZ MEDIA DEL CUADRADO DE LAS DESVIACIONES: 0cm (DESVIACIÓN TÍPICA)

    Portal 4: 4 personas, de las que mido sus alturas:

        150cm , 160cm, 190cm, 200cm ---> MEDIA:    175cm
                                         MEDIANA:  175cm

        -25      -15    15     25        MEDIA DESVIACIONES:  0
         25       15    15     25        MEDIA ABS DESVIACIONES:  20     Esto se llama en estadística DESVIACIÓN MEDIA (no se usa)
        625      225    225    625       MEDIA CUADRADO DE LAS DESV: 1300+450 = 1750 / 4 = 437.5cm2    : VARIANZA
                                         RAIZ MEDIA DEL CUADRADO DE LAS DESVIACIONES:  20.74cm (DESVIACIÓN TÍPICA)

                                         [ 175-20.74 = 154.26cm ,  175+20.74 = 195.74cm ]


    Tengo 4 portales TOTALMENTE DIFERENTES ENTRE SI, pero todos tienen la misma media y mediana.

    Cómo se interpreta la desv. típica: REGLA DE CHEVICHEV
    Si se abre un rango de una desv. típica alrededor de la media, siempre encontramos dentro al menos el 50% de los datos.
    Es decir, la mayor parte de la población.

    Tengo los expedientes que tardan de media 10.5 horas en procesarse con una desv. típica de 2.5 horas.
    Al menos el 50% (la mayor parte de los expedientes tardan entre 8 y 13 horas en procesarse).
    Lo cual no implica que haya expedientes que tarden más de 13 horas en procesarse.
    O que haya expedientes que tarden menos de 8 horas en procesarse.

    Eso si.. cómo hemos calculado la DESV. TIPICA? RAIZ MEDIA DEL CUADRADO DE LAS DIFERENCIA ENTRE CADA DATO Y LA MEDIA.
    Y qué pasa si la MEDIA no es representantiva de la población? Pues que la DESV. TÍPICA tampoco lo es.
    
    SOLO TRABAJO CON DESV. TIPICAS SI LA MEDIA ES REPRESENTATIVA:
    Si doy una media, doy su desv. típica.
    Si doy una mediana NO... doy otra cosa: Rango intercuartílico.

# Percentiles: MEDIDAS DE POSICION

   5 5 10 10 10 10 12 14 17         ...              MANOLO

   |-----------------------------------------------------|
                             ^
                             MEDIANA
               ^             ^             ^
               Q1            Q2            Q3   Cuartiles
   |-||||||||--|-------------|-------------|-------------|
    P1 P10 P20 P25          P50                PERCENTILES

    P90% Es el valor al que no llega el 90% de los datos.

    Si la tarea: aprobar un expediente tiene un P90 de 17 minutos. El 90% de los expedientes se aprueban en menos de 17 minutos.
    Muchas veces este dato me interesa muchísimo... El 90% 95%
    Hay casos raros.. y cuando optimizo, me interesa optimizar el grueso, la gran mayoría o los casos extremos?
    Depende...
    - A veces me interesa mejorar la mayor parte de los casos, y me interesa el P90 P95... ya que tendré con poco ahorro en cada caso, mucho ahorro acumulado
    - A veces me interesa mejorar los casos extremos, ya que al tardar tanto, si ahorro bastante en cada uno, consigo un ahorro importante.


En process mining no se trata de dar soluciones a los problemas.
Eso será otro tema... muy diferente... que competerá a otro tipo de profesionales.
A veces, mejoro un proceso cambiando el desarrollo de una app informática... y eso lo hace un desarrollador, UX.
A veces  mejoro un proceso documentándolo mejor... y eso lo hace un analista de negocio.
A veces, mejor un proceso rediseñándolo... y eso lo hace un ingeniero de procesos.

Nosotros, en process mining, lo que tratamos es de poner el foco en los problemas... no tratamos de resolverlos.
Eso será una segunda ronda.


    EXPEDIENTE

     Se da de alta   >  Se estudia  >  Se aprueba
                           v ^      >  Se cancela
                        Revisión

     Se da de alta   >  Se estudia  >  Revisa > Se estudia > Se revisa > Se estudia  >  Se aprueba
                                                                            v ^      >  Se cancela
                                                                            Revisión

---

Lo que genera pm4py al procesar nuestro conjunto de datos:

[
    {
        'attributes': {
             'concept:name': 1001
        }, 
        'events': [
            {
                'concept:name': 'Pedido recibido', 
                'time:timestamp': Timestamp('2025-06-01 09:00:00'), 
                'resource': 'Ana'
            }
            ,
            {
                'concept:name': 'Aprobación', 
                'time:timestamp': Timestamp('2025-06-01 11:30:00'), 
                'resource': 'Juan'
            }
        ]
    }, 
    {
        'attributes': {    
            'concept:name': 1002
        }, 
        'events': [
            {
                'concept:name': 'Pedido recibido', 
                'time:timestamp': Timestamp('2025-06-01 09:15:00'), 
                'resource': 'Ana'
            },
            {
                'concept:name': 'Rechazo', 
                'time:timestamp': Timestamp('2025-06-01 09:45:00'),
                'resource': 'Marta'
            }
        ]
    }
]