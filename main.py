import pandas 
import seaborn as sns
import matplotlib.pyplot as plt

### cargar data ###
filename = './tmdb_5000_movies.csv'
fileneme2 = './tmdb_5000_credits.csv'
movies = pandas.read_csv(filename, header=0)
credit = pandas.read.csv(filename2, header=0)
data = movies.merge(credit, on = 'title')
### Limpieza ###

## descriptivos del raw data set, chequeo nulos y duplicados
print(data.shape)
print(data.head().transpose())
print(data.dtypes) #concuerdan con el tipo de dato que quieren mostrar
print(data.isnull().sum()) #hay nulos
print("La cantidad de duplicados es:" , data.duplicated().sum())  #no hay duplicados

##nulos
dataClean = data
dataClean['homepage'].fillna('null',inplace= True) #ambos son strings no pasa nada si no tienen este campo
dataClean['tagline'].fillna('null',inplace= True) 
dataClean['overview'].fillna('null',inplace= True)
#elimino las filas de los que tienen nulos y no son significativos, en este caso 2 filas de release_date y 1 de runtime
dataClean.dropna(inplace= True)
print(dataClean.isnull().sum())


### analisis y graficos ###


top_movies = data.sort_values(by='revenue', ascending=False)
print(top_movies.head(10)[['title', 'revenue']])

top_movies = data.sort_values(by='budget', ascending=False)
print(top_movies.head(10)[['title', 'budget']])


# Duracion de pelicula preferida por la audiencia
run_pop=data.groupby('runtime')['popularity'].mean()
run_pop.plot(figsize = (10,8))
#title            
plt.title("Duracion preferida por la audiencia",fontsize=14)            
plt.xlabel('Runtime',fontsize = 13)
plt.ylabel('Popularity',fontsize = 13)
#max_value
max_run= run_pop.idxmax()

plt.show()

print('Duracion preferida por la audiencia', max_run, 'minutos.')


## las peliculas mas populares recaudan mas en box office? (grafico correlacion)
fig1 = sns.jointplot(x = "revenue", y = "popularity", kind = "scatter", data = data)
fig1.fig.suptitle('correlacion entre recaudacion y popularidad');
plt.show()

correlacion = data.corr()
print("Correlacion entre recaudacion y popularidad : ",correlacion.loc['revenue','popularity'])

## las peliculas con mayor budget son las que recaudan mas en box office?
fig2 = sns.jointplot(x = "revenue", y = "budget", kind = "scatter", data = data)
fig1.fig.suptitle('correlacion entre recaudacion y presupuesto');
plt.show()

correlacion = data.corr()
print("Correlacion entre recaudacion y presupuesto : ",correlacion.loc['revenue','budget'])




#popularidad de cada genero de pelicula (problema por como es la columna de genero en la db)
""""
popular_and_genres_data = data[['original_title', 'popularity', 'genres']]
mean_popular_vs_genre_data = popular_and_genres_data.groupby(['genres']).mean()
mean_popular_vs_genre_data = mean_popular_vs_genre_data.sort_values('popularity', ascending=False)
mean_popular_vs_genre_data.head()

mean_popular_vs_genre_data['popularity'].plot(stacked=False, kind='barh', figsize = (8,8),color='g');
plt.title('Genres classification by popularity', size=18)
plt.xlabel('popularity', size=12);
sns.set_style("whitegrid")
plt.show()
"""


#calculate Total Profits gained for all movies per year 
revenue_peryear = data.groupby(data['release_date'].dt.year)['revenue'].sum()

ax = revenue_peryear.plot(stacked=True, figsize=(10,8));
ax.set(xlabel='release year', ylabel='total revenue', title = 'Total revenue gained for all movies per year')
plt.show()

max_revenue= revenue_peryear.idxmax()

print('The movie industry made the highest profit in', max_revenue,'.')