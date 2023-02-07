import pandas as pd
import numpy as np
from sqlalchemy import create_engine


disney = pd.read_csv(r'C:\Users\DIEZ\Desktop\MySpace\Practicas\PI01_DATA05-main\Datasets\disney_plus_titles.csv')

disney['director'].fillna('Sin Dato', inplace = True)
disney['cast'].fillna('Sin Dato', inplace = True)
disney['country'].fillna('Sin Dato', inplace = True)
disney['rating'].fillna('Sin Dato', inplace = True)
disney['plataforma'] = 'disney'
disney['date_added'] = pd.to_datetime(disney['date_added'], format = '%B %d, %Y')


hulu = pd.read_csv(r'C:\Users\DIEZ\Desktop\MySpace\Practicas\PI01_DATA05-main\Datasets\hulu_titles.csv')

hulu['director'].fillna('Sin Dato', inplace = True)
hulu['cast'].astype(str)
hulu['country'].fillna('Sin Dato', inplace = True)
hulu['rating'].fillna('Sin Dato', inplace = True)
hulu['cast'].fillna('Sin Dato', inplace = True)
hulu['show_id'].fillna('Sin Dato', inplace = True)
hulu['type'].fillna('Sin Dato', inplace = True)
hulu['title'].fillna('Sin Dato', inplace = True)
hulu['release_year'].fillna(0, inplace = True)
hulu['duration'].fillna('Sin Dato', inplace = True)
hulu['description'].fillna('Sin Dato', inplace = True)
hulu['release_year'].astype(int)
hulu['plataforma'] = 'hulu'
hulu['date_added'] = pd.to_datetime(hulu['date_added'], format = '%B %d, %Y')


amazon = pd.read_csv(r'C:\Users\DIEZ\Desktop\MySpace\Practicas\PI01_DATA05-main\Datasets\amazon_prime_titles.csv')

amazon['director'].fillna('Sin Dato', inplace = True)
amazon['country'].fillna('Sin Dato', inplace = True)
amazon['rating'].fillna('Sin Dato', inplace = True)
amazon['cast'].fillna('Sin Dato', inplace = True)
amazon['show_id'].fillna('Sin Dato', inplace = True)
amazon['type'].fillna('Sin Dato', inplace = True)
amazon['title'].fillna('Sin Dato', inplace = True)
amazon['release_year'].fillna(0, inplace = True)
amazon['duration'].fillna('Sin Dato', inplace = True)
amazon['description'].fillna('Sin Dato', inplace = True)
amazon['release_year'].astype(int)
amazon['date_added'] = pd.to_datetime(amazon['date_added'], format = '%B %d, %Y')
amazon['plataforma'] = 'amazon'


netflix = pd.read_json(r'C:\Users\DIEZ\Desktop\MySpace\Practicas\PI01_DATA05-main\Datasets\netflix_titles.json')

netflix['director'].fillna('Sin Dato', inplace = True)
netflix['country'].fillna('Sin Dato', inplace = True)
netflix['rating'].fillna('Sin Dato', inplace = True)
netflix['cast'].fillna('Sin Dato', inplace = True)
netflix['show_id'].fillna('Sin Dato', inplace = True)
netflix['type'].fillna('Sin Dato', inplace = True)
netflix['title'].fillna('Sin Dato', inplace = True)
netflix['release_year'].fillna(0, inplace = True)
netflix['duration'].fillna('Sin Dato', inplace = True)
netflix['description'].fillna('Sin Dato', inplace = True)
netflix['release_year'].astype(int)
netflix['plataforma'] = 'netflix'
netflix['date_added'] = netflix['date_added'].str.lstrip()
netflix['date_added'] = netflix['date_added'].str.rstrip()
netflix['date_added'] = pd.to_datetime(netflix['date_added'], format = '%B %d, %Y')

"""
    Separamos la cantidad de minutos con la palabra min
"""
separacion_hulu = hulu['duration'].str.split(' ', n = 1, expand = True)
separacion_disney = disney['duration'].str.split(' ', n = 1, expand = True)
separacion_amazon = amazon['duration'].str.split(' ', n = 1, expand = True)
separacion_netflix = netflix['duration'].str.split(' ', n = 1, expand = True)

hulu['duration_int'] = separacion_hulu[0]
hulu['duration_str'] = separacion_hulu[1]

amazon['duration_int'] = separacion_amazon[0]
amazon['duration_str'] = separacion_hulu[1]

disney['duration_int'] = separacion_disney[0]
disney['duration_str'] = separacion_disney[1]

netflix['duration_int'] = separacion_netflix[0]
netflix['duration_str'] = separacion_netflix[1]


cadena_conexion = 'mysql+pymysql://root:123456789@localhost:3306/proyecto01'
conexion = create_engine(cadena_conexion)
conexion_ip = create_engine(cadena_conexion)

#Importamos la tabla a mysql con un nombre en especifico
def importar_tablas(archivo, nombre_archivo):
    
    archivo.to_sql(name = nombre_archivo , con = conexion_ip , index = False)

    
# Concatenamos todas la tablas a MYSQL   
def importar_Mysql(df1,df2,df3,df4, nombre_archivo):
    archivo = pd.concat([df1,df2,df3,df4])
    archivo.to_csv('peliculas')
    archivo.to_sql(name = nombre_archivo , con = conexion_ip , index = False)
    
# Concatenamos en un DataFrame los 4 datasets
peliculas = pd.concat([disney,hulu,amazon,netflix])

#Cargamos el dataset listo para convetirlo en un CSV
carga= r'C:\Users\DIEZ\Desktop\MySpace\Practicas\PI01_DATA05-main\peliculas.csv'
peliculas.to_csv(carga,index = False, encoding = 'utf-8') 


