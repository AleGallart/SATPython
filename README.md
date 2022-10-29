# SATPython
Repositorio para TP final

Para este trabajo, nos planteamos explorar y analizar una extensa base de datos de peliculas para lograr identificar cuales son las caracteristicas que definen su exito comercial.
Para ello, identificamos a la columna 'revenue' (recaudacion) como la principal metrica que define tal exito.
Como hipotesis, decidimos plantear ciertas caracteristicas de las peliculas como las que, en efecto, influyen sobre cual es el rendiiento final de la pelicula en 'box office'. Estas son:
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
En efecto, con el primer grafico vemos que existe una correlacion positiva bastante alta, especificamente de 0,73.
COn el segundo grafico, observamos que la cantidad de revenue total y el budget va subiendo progresivamente a medida que pasan los años. Esto sugiere que cuanto mas actual es la pelicula, mayor es el revenue y su presupuesto. Igualmente, hay que tener en cuenta que no se esta mostrando cuantas peliculas hay en cada año. Quizas los años mas recientes tienen una mayor cantidad de peliculas, y por eso su revenue y budget total es considerablemente mayor.

4.2
En segundo lugar, buscamos identificar un vinculo entre revenue y genero de pelicula. En este caso, realizamos un grafico de barras mostrando la cantidad de revenue recaudado por cada genero. Se destacan Accion, Aventura y, en menor medida, Comedia. Para este caso, si decidimos mostrar tambien cuantas peliculas tiene cada genero. Lo que nos mostro estos dos graficos combinados es que las peliculas de Accion y Aventura son, en terminos generales, las que mas recaudan, ya que no son las que mas peliculas tienen pero si las que mas alto tienen el revenue total.

4.3
En cuanto a la popularidad de la pelicula, tambien encontramos que eiste una correlacion positiva del 0,64, lo que indiciaria que cuanto mas popular se considera la pelicula, mas recauda. Es importante tener en cuenta, igualmente, que no es una relacion lineal positiva perfecta.

4.4

4.5

4.6
La siguiente parte de nuestro analisis consistio en establecer la relacion entre el revenue y la duracion de las peliculas. Con el grafico en cuestion, es posible notar que existe una tendencia a encontrar recaudaciones mas altas cuando el 'runtime' se encuentra entre los valores 140 y 200. De todas formas, esto no se puede ver de forma tan clara en el grafico, por lo que no creemos que la informacion a disposicion no es lo suficientemente clara como para afirmar que la duracion de las peliculas tiene un efecto real en el dinero recaudado en box office.

4.7
Por el lado del revenue junto con el rating de votacion, vemos en el grafico que existe una tendencia clara a que, a medida que el promedio de votacion sube, el revenue recaudado tambien. La baja pronunciada luego del vote_average 8 consideramos que ocurre por un tema de falta de datos, ya que no existen muchas peliculas con rating superior a 8.
Podriamos decir que esto demuestra que, cuanto mas alto es el rating de la pelicula (puesto por el publico), mas dinero se espera que recaude finalmente.

En el grafico posterior, buscamos mostrar como va evolucionando el rating promedio de las peliculas a medida que pasan los años. En lineas generales, el voto promedio del publico ha ido bajando ha medida que pasaron los años. Esto significaria, continuando con el analisis del grafico anterior, que se espera que la recaudacion promedio por cada pelicula baje, al menos en el caso de que los ratings de las peliculas continuen su tendencia a bajar.


