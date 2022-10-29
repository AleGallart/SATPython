# SATPython
Repositorio para TP final

Para este trabajo, nos planteamos explorar y analizar una extensa base de datos de peliculas para lograr identificar cuales son las caracteristicas que definen su exito comercial.
Para ello, identificamos a la columna 'revenue' (recaudacion) como la principal metrica que define tal exito.
Como hipotesis, decidimos plantear ciertas caracteristicas de las peliculas como las que, en efecto, influyen sobre cual es el rendimiento final de la pelicula en 'box office'. Estas son:
- Budget (Presupuesto)
- Genre (Genero)
- Popularity (Popularidad)
- Production_countries (Pais de produccion)
- Production_companies (Compania de produccion)
- Runtime (Duracion de la pelicula)
- Vote_average (Rating promedio)
- Release_year (año de lanzamiento)

Luego del analisis, buscaremos estar en condiciones de indentificar si efectivamente estos atributos de las peliculas tienen una influencia clara en el exito comercial o no.

Analisis:

4.1
En primer lugar, planteamos la relacion entre revenue y budget. En principio, diriamos que hay una correlacion clara que indica que cuanto mas presupuesto tiene una pelicula, mas va a recaudar. 
En efecto, con el primer grafico vemos que existe una correlacion positiva alta, especificamente de 0,73.
Con el segundo grafico, observamos que la cantidad de revenue total y el budget va subiendo progresivamente a medida que pasan los años. Esto sugiere que cuanto mas actual es la pelicula, mayor es el revenue y su presupuesto. Igualmente, hay que tener en cuenta que no se esta mostrando cuantas peliculas hay en cada año. Quizas los años mas recientes tienen una mayor cantidad de peliculas, y por eso su revenue y budget total es considerablemente mayor.

4.2
En segundo lugar, buscamos identificar un vinculo entre revenue y genero de pelicula. En este caso, realizamos un grafico de barras mostrando la cantidad de revenue recaudado por cada genero. Se destacan Animacion, Aventura y fantasia. Para este caso, si decidimos mostrar tambien cuantas peliculas tiene cada genero. Lo que nos mostro estos dos graficos combinados es que las peliculas de Accion y Aventura son, en terminos generales, las que mas recaudan, ya que no son las que mas peliculas tienen pero si las que mas alto tienen el revenue total.

4.3
En cuanto a la popularidad de la pelicula, tambien encontramos que eiste una correlacion positiva del 0,64, lo que indiciaria que cuanto mas popular se considera la pelicula, mas recauda. Es importante tener en cuenta, igualmente, que no es una relacion lineal positiva perfecta.

4.4
En este caso hubo un gran desafio ya que la lista de valores unica era muye extensa por lo que debio hacerce una funcion que ordene de mayor a menor y solo deje una cantidad n de resultados. La conlcusion fue que las companias con mayor revene promedio por pelicula no son parte de las principales companias (las que mayor revenue total mueven por ciclo anual)

4.5
Se puede obseervar que hay una concentreacion muy grande en estados unidos, pero esto puede deberse en parte a que la fuente de datos proviene de este pais. Destaca como ciertos paises donde la cantidad de peliculas grabadas es muy baja tambien es el lugar donde mas revenue por pelicula se alcanza. Esto se pude explicar en parte porque si una compania tiene que tener un presupuesto muy alto para hacer una filmacion en una ubicacion muy remota, y como ya se vio el prespeusto tiene una realcion con el revenue de la pelicula.

4.6
La siguiente parte de nuestro analisis consistio en establecer la relacion entre el revenue y la duracion de las peliculas. Con el grafico en cuestion, es posible notar que existe una tendencia a encontrar recaudaciones mas altas cuando el 'runtime' se encuentra entre los valores 140 y 200. De todas formas, esto no se puede ver de forma tan clara en el grafico, por lo que no creemos que la informacion a disposicion no es lo suficientemente clara como para afirmar que la duracion de las peliculas tiene un efecto real en el dinero recaudado en box office.

4.7
Por el lado del revenue junto con el rating de votacion, vemos en el grafico que existe una tendencia clara a que, a medida que el promedio de votacion sube, el revenue recaudado tambien. La baja pronunciada luego del vote_average 8 consideramos que ocurre por un tema de falta de datos, ya que no existen muchas peliculas con rating superior a 8.
Podriamos decir que esto demuestra que, cuanto mas alto es el rating de la pelicula (puesto por el publico), mas dinero se espera que recaude finalmente.

En el grafico posterior, buscamos mostrar como va evolucionando el rating promedio de las peliculas a medida que pasan los años. En lineas generales, el voto promedio del publico ha ido bajando ha medida que pasaron los años. Esto significaria, continuando con el analisis del grafico anterior, que se espera que la recaudacion promedio por cada pelicula baje, al menos en el caso de que los ratings de las peliculas continuen su tendencia a bajar.


Conclusión general, dificultades y próximos pasos: 

El análisis nos permitió corroborar algunas de nuestras presunciones iniciales, ya que varias de las características analizadas si parecieron mostrar que tenían una relacion marcada con la cantidad de dinero recaudada. Igualmente, creemos que hay muchos otros factores que influyen, en especial variables como el actor/actores principales y el director de la película, que merecen ser considerados, ya que como espectadores es una de las primeras cosas que analizamos antes de ir a ver una película.
El manejo de los datos fue muy desafiante ya que se necesito modificar los tipos de datos para que concuerden con el tipo de dato que les correspondia, como fue el caso de la fecha y los diccionarios (los cuales se bajaban del archivo .csv como un string). Tambien se hizo uso de varias funciones para poder agrupar las columnas que se manejaban con objetos como diccionario, lo cual agregaba una gran complejidad al agregar dimensiones a las columnas.
No se exploraron modelos estadisticos avanzados para probar las realciones entre las variables independientes y la variable dependiente propuesta (revenue). Tambien no se analizaron las relaciones entre las variables independientes donde se podrian buscar relaciones como colinearidad. Es por esto que sugerimos, a quien lea este proyecto y se note interesado por la temática, que busque expandir el análisis a nuevas variables y, de ser posible, adentrarse aun mas otras relaciones planteadas aquí que no han quedado del todo claras, como por ejemplo la de revenue con duración de las películas.


