"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """
import config
from time import process_time
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria
"""

# -----------------------------------------------------
# API del TAD Catalogo de peliculas
# -----------------------------------------------------
#325001
#2003
def newCatalog():

    catalog = {'movies': None,
               'ids': None
               }

    catalog['movies'] = lt.newList('ARRAY_LIST',compareRecordIds)
    catalog['ids'] = mp.newMap(325001,
                                   maptype='CHAINING',
                                   loadfactor=1.0,
                                   comparefunction=compareMapMoviesIds)

    
    return catalog



# Funciones para agregar informacion al catalogo

def addmovie(catalog, movie):
    lt.addLast(catalog['movies'], movie)
    mp.put(catalog['ids'], int(movie['\ufeffid']), movie)


# ==============================
# Funciones de consulta
# ==============================

def obtener_primera_pelicula(catalog):
    return mp.get(catalog["ids"],2)
def obtener_ultima_pelicula(catalog):
    return (mp.get(catalog["ids"],3026))

def datos_pelicula(obtener_primera_pelicula,obtener_ultima_pelicula):
    titulo=obtener_primera_pelicula["value"]["title"]
    fecha_estreno=obtener_primera_pelicula["value"]["release_date"]
    promedio_votacion=obtener_primera_pelicula["value"]["vote_average"]
    idioma=obtener_primera_pelicula["value"]["spoken_languages"]
    
    titulo2=obtener_ultima_pelicula["value"]["title"]
    fecha_estreno2=obtener_ultima_pelicula["value"]["release_date"]
    promedio_votacion2=obtener_ultima_pelicula["value"]["vote_average"]
    idioma2=obtener_ultima_pelicula["value"]["spoken_languages"]
    return (titulo,fecha_estreno,promedio_votacion,idioma,titulo2,fecha_estreno2,promedio_votacion2,idioma2)


# ==============================
# Funciones de Comparacion
# ==============================

def compareRecordIds(recordA, recordB):
    if int(recordA['\ufeffid']) == int(recordB['\ufeffid']):
        return 0
    elif int(recordA['\ufeffid']) > int(recordB['\ufeffid']):
        return 1
    return -1
    
def compareMapMoviesIds(id, entry):
    """
    Compara dos ids de películas, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

        