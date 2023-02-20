#-------------------------------------------------------------------------------
# Nombre: Proyecto Individual 1 
# Titulo: Machine Learning Operations (MLOps)
# Author:Jose Manuel Bracho Navarro
# Fecha:     14/02/2023
#-------------------------------------------------------------------------------
from typing import Union
from fastapi import FastAPI
import pandas as pd
import numpy as np
from collections import Counter

datos = pd.read_csv("Datos_PI.csv")

#Creo la aplicacion
app = FastAPI()

@app.get('/')
def presentacion():
    return 'Bienvenidos a mi Proyecto Individual 01 - Bracho Navarro, Jose Manuel'

@app.get("/contacto")
def contacto():
    return "Email: josemanuelbrachonavarro@gmail.com / Linkedin: www.linkedin.com/in/jose-manuel-bracho-navarro-35010324a"

#-------------------------------------------------------------------------------
# 1. Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. 
#    (la función debe llamarse get_max_duration(year, platform, duration_type))
#-------------------------------------------------------------------------------

@app.get("/max_duration/{year}/{platform}/{duration_type}")
def get_max_duration(year:int, platform:str, duration_type:str):
    if duration_type and (str(duration_type).lower() in ['season', 'min']):
        platform_names = {
            'n': 'netflix',
            'h': 'hulu',
            'd': 'disney+',
            'as': 'amazon'
        }
        platforms = list(platform_names.keys()) if not platform else [platform]
        resultados = []
        for plat in platforms:
            datos_loc = datos[datos['id'].str.startswith(plat, na=False)]
            datos_loc = datos_loc[datos_loc['duration_type'] == duration_type]
            datos_loc = datos_loc[datos_loc['release_year'] == year] if year else datos_loc
            datos_loc = datos_loc.sort_values(by='duration_int', ascending=False, na_position='last')
            if not datos_loc.empty:
                resultados.append({
                    "plataforma": platform_names[plat],
                    "año": str(datos_loc.iloc[0]['release_year']),
                    "nombre": datos_loc.iloc[0]['title'],
                    "duracion": str(datos_loc.iloc[0]['duration_int'])
                })
        return resultados
    else:
        return {"mensaje": "Error, parámetros incorrectos"}


#-------------------------------------------------------------------------------
# 2. Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
#  (la función debe llamarse get_score_count(platform, scored, year))
#-------------------------------------------------------------------------------

@app.get('/get_score_count/{platform}/{score}/{year}')
def get_score_count(platform:str, score:float, year:int):
    if platform in ['n','d','h','as'] and int(score) == score and int(year) == year:         # Selecciona sólo las filas donde el id comience con la plataforma, score y ano sea el especificado
        datos_loc = datos[datos['id'].str.startswith(platform, na=False)]
        datos_loc = datos_loc[datos_loc['ScoreMedia'] > score]
        datos_loc = datos_loc[datos_loc['release_year'] == year]
        
        platform_name = '' # Asigna el nombre completo de la plataforma

        if platform == 'n':
            platform_name = 'Netflix'
        elif platform == 'd':
            platform_name = 'Disney'
        elif platform == 'h':
            platform_name = 'Hulu'
        elif platform == 'as':
            platform_name = 'Amazon'

        count = datos_loc.shape[0]                                                                # Cuenta el número de películas que cumplen con los criterios
        return {"platform": platform_name, "score >": score, "year": year, "count": count}        # Devuelve un diccionario con los resultados
    else:
        return {"message":"Error, invalid parameters"}



#-------------------------------------------------------------------------------
# 3. Cantidad de películas por plataforma con filtro de PLATAFORMA.
#  (La función debe llamarse get_count_platform(platform))
#-------------------------------------------------------------------------------
@app.get('/get_count_platform/{platform}')      
def get_count_platform(platform:str):
    if platform.lower() in ['amazon', 'a', 'netflix', 'n', 'hulu', 'h', 'disney', 'd']:  # Verifica si el valor recibido está en la lista de plataformas válidas
        if platform.lower() in ['amazon', 'a']:
            datos_loc = datos[datos['id'].str.startswith('a', na=False)]
            nombre = 'Amazon'
        elif platform.lower() in ['netflix', 'n']:
            datos_loc = datos[datos['id'].str.startswith('n', na=False)]
            nombre = 'Netflix'
        elif platform.lower() in ['hulu', 'h']:
            datos_loc = datos[datos['id'].str.startswith('h', na=False)]
            nombre = 'Hulu'
        elif platform.lower() in ['disney', 'd']:
            datos_loc = datos[datos['id'].str.startswith('d', na=False)]
            nombre = 'Disney'
        
        respuesta = {"plataforma":nombre,                                   # Se retorna un diccionario con la información de la plataforma y la cantidad de elementos en datos_loc
                     "cantidad":datos_loc.shape[0]
                    }                                                       # Si el valor recibido no es una plataforma válida, se retorna un mensaje de error
        return respuesta                                                    
    else:
        return {"message":"Error, plataforma incorrecta"}


#-------------------------------------------------------------------------------
# 4. Actor que más se repite según plataforma y año. 
# (La función debe llamarse get_actor(platform, year))
#-------------------------------------------------------------------------------
@app.get('/get_actor/{platform}/{year}')
def get_actor(platform:str, year:int):  #Se asigna el nombre de la plataforma
    if platform.lower() in ['amazon', 'a', 'netflix', 'n', 'hulu', 'h', 'disney', 'd']:
        if platform.lower() in ['amazon', 'a']:
            platform_name = 'Amazon'
        elif platform.lower() in ['netflix', 'n']:
            platform_name = 'Netflix'
        elif platform.lower() in ['hulu', 'h']:
            platform_name = 'Hulu'
        elif platform.lower() in ['disney', 'd']:
            platform_name = 'Disney'
        
         #Se filtra en el dataframe segun plataforma y ano, utilizando el metodo loc

        datos_loc = datos[datos['id'].str.startswith(platform_name[0].lower(), na=False)]
        datos_loc = datos_loc[datos_loc['release_year'] == year]
        datos_loc = datos_loc[datos_loc['cast'].notnull()]
        datos_loc['cast'] = datos_loc['cast'].apply(lambda x: x.split(',')) #Se aplica lambdapara convertir cada elemento de la columna en una lista separada de actores
        all_actors = [actor for actors in datos_loc['cast'].tolist() for actor in actors] #Se crea una lista con todos los actores de todas las peliculas disponibles en la plataforma y ano especificado
        counter = Counter(all_actors) #Se cuenta la frecuencia de cada actor en la lista 'all_actors'
        most_common_actor = counter.most_common(1)[0][0] #Se obtiene el actor mas repetido
        return {"platform": platform_name, "year": year, "actor": most_common_actor}
    else:
        return {"message":"Error, plataforma incorrecta"}



