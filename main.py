import pandas 

### cargar data ###
filename = './tmdb_5000_movies.csv'
data = pandas.read_csv(filename, header=0)


### Limpieza ###

## descriptivos del raw data set, chequeo nulos y duplicados
print(data.shape)
print(data.head(10))
print(data.dtypes)
print(data.isnull().sum()) #hay nulos
print(data.duplicated().sum())  #no hay duplicados

##nulos
dataClean = data
dataClean['homepage'].fillna('null',inplace= True) #ambos son strings no pasa nada si no tienen este campo
dataClean['tagline'].fillna('null',inplace= True) 
dataClean['overview'].fillna('null',inplace= True)
#elimino las filas de los que tienen nulos y no son significativos, en este caso 2 filas de release_date y 1 de runtime
dataClean.dropna(inplace= True)
print(data1.isnull().sum())



