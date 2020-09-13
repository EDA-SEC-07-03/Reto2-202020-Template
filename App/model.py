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
import controller as ctr
import csv
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from time import process_time
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

    catalog = {"movies":None,'ids': None,"productora":None
                }
    catalog["movies"]=lt.newList("ARRAY_LIST")

    catalog['ids'] = mp.newMap(30,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   comparefunction=compareMapMoviesIds)
    catalog["productora"]= mp.newMap(30,
                                   maptype='PROBING',
                                   loadfactor=0.5,
                                   comparefunction=1)

    
    return catalog



# Funciones para agregar informacion al catalogo

def addmovie(catalog, movie):
    mp.put(catalog['ids'], int(movie['id']), movie)
    catalog["movies"]


# ==============================
# Funciones de consulta
# ==============================

def obtener_primera_pelicula(catalog):
    return mp.get(catalog["ids"],2)
def obtener_ultima_pelicula(catalog):
    return (mp.get(catalog["ids"],469219))

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
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
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
def compareMapMoviesCompany(id=5,entry={"key":3,"value":"hola"}):
    """
    Compara dos ids de películas, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    print(identry)

#compareMapMoviesCompany()

#_________________________________________________________________________

def loadCSVFile (file,catalog):
    dialect = csv.excel()
    dialect.delimiter=";"
    with open( config.data_dir + file, encoding="utf-8") as csvfile:
        row = csv.DictReader(csvfile, dialect=dialect)
        for elemento in row: 
            addmovie(catalog,elemento)
    return catalog

def load_productora_first(file,catalogo,xd):
    dialect = csv.excel()
    dialect.delimiter=";"
    with open( config.data_dir + file, encoding="utf-8") as csvfile:
        row = csv.DictReader(csvfile, dialect=dialect)
        if(xd == 0):
            for elemento in row:
                if():

        
vacio=newCatalog()
catalogox= loadCSVFile("SmallMoviesDetailsCleaned.csv",vacio)
xdasd=load_productora_first("SmallMoviesDetailsCleaned.csv",vacio,0)