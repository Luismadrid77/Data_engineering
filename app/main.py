import pandas as pd
from fastapi import FastAPI
app = FastAPI()
def listaPalabrasDicFrec(listaPalabras):
    frecuenciaPalab = [listaPalabras.count(p) for p in listaPalabras]
    return dict(list(zip(listaPalabras, frecuenciaPalab)))
def ordenaDicFrec(dicFrec):
    aux = [(dicFrec[key], key) for key in dicFrec]
    aux.sort()
    aux.reverse()
    return aux
@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get('/validar/{numero}')
def validar_capicua(numero:str):
    respuesta = 'No es capicua'
    if numero == numero[::-1]:
        respuesta = 'Si es capicua'
    return {
        'numero':numero,
        'validacion':respuesta
    }
@app.get('/get_max_duration')
def get_max_duration(anio:int, plat:str, dtype:str):
    data = pd.read_csv('https://raw.githubusercontent.com/Luismadrid77/Data_engineering/main/peliculas.csv')
    data.duration_int = pd.to_numeric(data.duration_int, errors='coerce')
    data.release_year = pd.to_numeric(data.release_year, errors='coerce')
    query1 = data[(data['release_year'] == anio) & (data['plataforma'] == plat) & (data['duration_type'] == dtype)]
    query1 = query1.sort_values('duration_int', ascending=False)
    res = query1.head(1)
    res = res.title.to_list()
    return 'El fim que mas duro fue: ', str(''.join(res))
@app.get('/get_count_plataforma')
def get_count_plataforma(plat:str):
    data = pd.read_csv('https://raw.githubusercontent.com/Luismadrid77/Data_engineering/main/peliculas.csv')
    query2 = data['plataforma'] == plat
    count_query2 = data[query2]['type'].value_counts()
    return {'Plataforma':plat,
            'Movies':str(count_query2[0]),
            'Tv show':str(count_query2[1])
            }
@app.get('/get_listedin')
def get_listed_in(categoria:str):
    df = pd.read_csv('https://raw.githubusercontent.com/Luismadrid77/Data_engineering/main/peliculas.csv')
    plataforma = ""
    plats = df.plataforma.unique()
    max = 0
    for plat in plats:
        if df[df.plataforma==plat].listed_in.str.count(categoria).sum() > max:
            max = df[df.plataforma==plat].listed_in.str.count(categoria).sum()
            plataforma = plat
    return f"La plataforma con más titulos listados en el genero {categoria} es: {plataforma} con un total de {max} titulos"
@app.get('/get_actor')
def get_actor(plat:str, anio:int):
    data = pd.read_csv('https://raw.githubusercontent.com/Luismadrid77/Data_engineering/main/peliculas.csv')
    act = data[(data['plataforma'] == plat) & (data['release_year'] == anio)].cast.str.split(',')
    act = act.dropna()
    actores_año = []
    for actores in act:
        for actor in actores:
            actor = actor.rstrip()
            actor = actor.lstrip()
            actores_año.append(actor)
    actor = listaPalabrasDicFrec(actores_año)
    actor = ordenaDicFrec(actor)
    return f'El actor que mas se repite en: {plat} en el año: {anio} es: {actor[0][1]} con un total de: {actor[0][0]} apariciones'