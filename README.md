Generación de poligonal a partir de imágenes de dron.

Imágenes de dron

Osvaldo Barajas Amezcua, Estefanía Guadalupe Hernández Aldrete.

  Campus Coquimatlán, 28400, [obarajas2@ucol.mx](mailto:obarajas2@ucol.mx),  ehernandez21@ucol.mx.

Resumen

Se presenta un programa que tiene como objetivo obtener un polígono en base a coordenadas geográficas con imágenes tomadas con dron.

**Palabras clave** : Programa, coordenadas geográficas, fotografía.

Abstract

A program that aims to obtain a polygon based on geographical coordinates with images taken with drone is presented.



**Keywords** : Program, Geographic coordinates, photograph.

1. INTRODUCCIÓN

En este proyecto se pretende realizar un programa en el cual se obtenga un polígono con coordenadas geográficas mediante fotografías.

Este con la finalidad de crear un programa de gran utilidad para nosotros y demás generaciones como también en nuestra área de trabajo y estudio para facilitar la realización de un polígono

2. DESARROLLO

Lo que desarrollaremos en este programa se llevará a cabo en el software GeoSetter, en el cual obtendremos los metadatos(resolución en pixeles, coordenadas, lugar, fecha, hora, etc) de las fotografías.

Una vez obtenidos los datos necesarios de las fotografías, realizaremos una agenda tomando en cuenta los datos ya mencionados previamente. En nuestro archivo de Python haremos que el código mande a llamar a la agenda y con las coordenadas que se muestran en la agenda plotear un polígono mediante la librería matplotlip.

Con todo esto obtendremos la dirección que tuvo el dron al momento de tomar las imágenes.

2.1. **GeoSetter**

GeoSetter es una aplicación gratuita para Windows con la que podrás geolocalizar tus fotos en un mapa, obteniendo sus coordenadas GPS.

Geolocalizar una foto es tan fácil como seleccionarla y navegar por el mapa hasta encontrar su emplazamiento. El programa se encarga de rescatar los datos del mapa y guardarlos en los metadatos de la imagen.

Existen distintos tipos de mapas, simbólicos y gráficos, gracias a los mapas de Google.

El programa permite editar otros metadatos de las imágenes como, por ejemplo, la fecha de creación.

GeoSetter permite también la exportación a Google Earth y a Locr.

![Imagen1](https://raw.githubusercontent.com/Osvaldo-Barajas/Proyecto-Programacion/master/GEOSETTER.jpg)


2.2. Preparación del código

![Imagen1](https://raw.githubusercontent.com/Osvaldo-Barajas/Proyecto-Programacion/master/Imagenes/codigo.png)
 
3.Manejo de datos

Con el uso de los datos, que son coordenadas geográficas obtenidas con ayuda de un dron, (imágenes) esto para la realización de un código en Python que nos ayude a generar un polígono, con base a los datos.

De acuerdo a como se va graficando el polígono, sabremos la dirección que tuvo que tomar el Dron, para generar las imágenes con los metadatos.

Al saber la dirección que tomo el dron, nos dará referencias de los límites geográficos de nuestro polígono, será de ayuda al momento de georreferenciarnos.

4.Resultados

Los resultados obtenidos gracias al siguiente código y a los datos (coordenadas geográficas) obtuvimos una poligonal de tipo abierta es el terreno trabajo con el dron.

Coordenadas:

![Imagen1](https://raw.githubusercontent.com/Osvaldo-Barajas/Proyecto-Programacion/master/Imagenes/coordenadas.png)

Código:

![Imagen1](https://raw.githubusercontent.com/Osvaldo-Barajas/Proyecto-Programacion/master/Imagenes/codigo.png)

Con la librería matplottlib obtuvimos el grafico de la poligonal abierta trabajada con las fotografías aéreas.

Gráfico de la poligonal:

![Imagen 1](https://github.com/Osvaldo-Barajas/Proyecto-Programacion/blob/master/Imagenes/poligonal.png)

Otro resultado a destacar es que podemos conocer la trayectoria que tomó el dron para realizar las fotografías, que fue del punto a la x marcada en el gráfico.

5.Conclusión

Concluimos que los ingenieros Topógrafos Geomáticos son aquellas personas que día con día deben mejorar sus técnicas de trabajo y pues claramente la programación es una forma muy innovadora de hacer las cosas mucho más fáciles y efectivas.

Este tipo de proyectos tal vez nos hacen sufrir, pero nos demuestran de que estamos hechos, en este proyecto de análisis de estructuras combinado con la programación de Python hemos concluido que la complejidad de los programas a veces es alta y más para nosotros que apenas llevamos las bases, durante este camino tuvimos obstáculos en la programación más sin embargo lo pudimos superar.

Python es una herramienta muy útil cuenta con bastantes librerías que te ayudan a la hora de estar trabajando. Al final de todo pudimos comprobar que si es posible dicho traspase de información. Nos sentimos muy orgullosos de haber concluido este proyecto satisfactoriamente además de que nos vamos con una herramienta que nos puede ser de utilidad durante toda nuestra carrera.

6. Referencias

Delclaux, Isidoro; Seoane, Julio (1982). Psicología cognitiva y procesamiento de la información: teoría, investigación y aplicaciones. Madrid: Ediciones Pirámide, 1982.

Ellis, David (1992a). The physical and cognitive paradigms in Information Retrieval Re search. // Journal of Documentation. 48:1 (March 1992) 45-46.

Markey, Karen (1990). Keyword searching in an online catalog enhanced with a library classification. // Bengtson, Betty G.; Hill, Janet Swan (eds.). Classification of library materials: current and future potential for providing access. New York: Neal-Shuman Publishers, 1990. 99-125.

Sagredo Fernández, Félix; Espinosa Temiño, María Blanca (2000). Del libro, al libro electrónico-digital. // Cuadernos de Documentación Multimedia. 9 (2000).

Smith, Ph. J.; Beghtol, C.; Fidel, R.; Kwasnik, B. H. (eds.) (1993). Proceedings of the 4th ASIS SIG/CR Classification Research Workshop: Columbus, OH, Oct.24, 1993. Silver Spring, MD.: American Society for Information Science, 1993.

POSTER:

![Imagen2](https://raw.githubusercontent.com/Osvaldo-Barajas/Proyecto-Programacion/master/Imagenes/POSTER.png)
