import pandas 

## cargar data
filename = './tmdb_5000_movies.csv'
data = pandas.read_csv(filename, header=0)

## descriptivos del raw data set
print(data.shape)
print(data.head(10))
data.info()  #se puede ver que hay nulos
print(data.describe())

#veo nulos
print(data.isnull().sum())
print(data.dtypes)
#data.fillna('null',inplace= True) #el problema es que deberia remplazar los strings por un string y los numeros por numeros
#print(data.isnull().sum())

## duplicados 
print(data.duplicated().sum()) #no hya duplicados


#agrego esto para pushear