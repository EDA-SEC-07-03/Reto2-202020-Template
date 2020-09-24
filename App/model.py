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

    catalog = {"movies":None,"casting":None,'ids': None,"productora":None,"genero":None,"pais":None
                }
    catalog["movies"]=lt.newList("ARRAY_LIST",compareRecordIds)

    catalog["casting"]=mp.newMap(350000,
                                   maptype='CHAINING',
                                   loadfactor=1.0,
                                   comparefunction=compareMapMovieIds)
    
    catalog["genero"]=mp.newMap(23,maptype='CHAINING',
                                   loadfactor=1.0,
                                   comparefunction=compare_companies_byname)
    catalog["pais"]=mp.newMap(197,maptype='CHAINING',
                                   loadfactor=1.0,
                                   comparefunction=compare_companies_byname)
    
    catalog['ids'] = mp.newMap(350000,
                                   maptype='CHAINING',
                                   loadfactor=1.0,
                                   comparefunction=compareMapMovieIds)
    catalog["productora"]= mp.newMap(35000,
                                   maptype='CHAINING',
                                   loadfactor=1.0,
                                   comparefunction=compare_companies_byname)
    catalog["actor"]= mp.newMap(350000,
                                   maptype='CHAINING',
                                   loadfactor=1.0,
                                   comparefunction=compare_companies_byname)                               

    
    return catalog

# Funciones para agregar informacion al catalogo

def addmovie(catalog, movie):
    mp.put(catalog['ids'], int(movie["\ufeffid"]), movie)

def addcasting(catalog,casting):
    mp.put(catalog["casting"],int(casting["id"]),casting)

def addmovie_company(catalogo,nombre_compañia,pelicula):
    companies=catalogo["productora"]
    existe_compañia=mp.contains(companies,nombre_compañia)
    if(existe_compañia):
        entry = mp.get(companies, nombre_compañia)
        companie= me.getValue(entry)
    else:
        companie = newCompanie(nombre_compañia)
        mp.put(companies, nombre_compañia, companie)
    lt.addLast(companie['pelicula'], pelicula)

    cmpavg = companie['vote_average']
    movieavg = pelicula['vote_average']
    if (movieavg == 0.0):
        companie['vote_average'] = float(movieavg)
    else:
        companie['vote_average'] = (cmpavg + float(movieavg)) / 2
        
def addmovie_genre(catalogo,nombre_genero,pelicula):
    generos=catalogo["genero"]
    existe_genero=mp.contains(generos,nombre_genero)
    if(existe_genero):
        llave_valor=mp.get(generos,nombre_genero)
        valor=me.getValue(llave_valor)
    else:
        valor = newCompanie(nombre_genero)
        mp.put(generos, nombre_genero, valor)
    lt.addLast(valor["pelicula"],pelicula)
    cmpavg = valor['vote_average']
    movieavg=pelicula["vote_average"]
    if(movieavg == 0.0):
        valor["vote_average"]=float(movieavg)
    else:
        valor['vote_average'] = (cmpavg + float(movieavg)) / 2
def addmovie_director(catalog, nombre_director, casting):
    director = catalog["actor"]
    pos_pelicula = int(casting["id"])
    pelicula = me.getValue(mp.get(catalog["ids"], pos_pelicula))
    existe_director = mp.contains(director,nombre_director)
    if existe_director:
        llave_valor = mp.get(actor, nombre_director)
        valor = me.getValue(llave_valor)
    else:
        valor = newCompanie(nombre_director)
        mp.put(actor, nombre_director, valor)

    lt.addLast(valor["pelicula"],pelicula)
    promedio = valor["vote_average"]
    pro_movie = pelicula["vote_average"]
    if(pro_movie == 0.0):
        valor["vote_average"]=float(pro_movie)
    else:
        valor['vote_average'] = (promedio + float(pro_movie)) / 2
def addmovie_actor(catalog, nombre_actor, casting):
    actor = catalog["actor"]
    pos_pelicula = int(casting["id"])
    pelicula = me.getValue(mp.get(catalog["ids"], pos_pelicula))
    existe_actor = mp.contains(actor,nombre_actor)
    if existe_actor:
        llave_valor = mp.get(actor, nombre_actor)
        valor = me.getValue(llave_valor)
    else:
        valor = newCompanie(nombre_actor)
        mp.put(actor, nombre_actor, valor)

    lt.addLast(valor["pelicula"],pelicula)
    promedio = valor["vote_average"]
    pro_movie = pelicula["vote_average"]
    if(pro_movie == 0.0):
        valor["vote_average"]=float(pro_movie)
    else:
        valor['vote_average'] = (promedio + float(pro_movie)) / 2
    

def addmovie_pais(catalogo,nombre_pais,pelicula):
    pais=catalogo["pais"]
    pos_director=int(pelicula["\ufeffid"])
    existe_pais=mp.contains(pais,nombre_pais)
    director=me.getValue(mp.get(catalogo["casting"],pos_director))
    pelicula["director"]=director
    if(existe_pais):
        llave_valor=mp.get(pais,nombre_pais)
        valor=me.getValue(llave_valor)
    else:
        valor=newMovieCountry(nombre_pais)
        mp.put(pais,nombre_pais,valor)
    lt.addLast(valor["peliculas"],pelicula)

def newMovieCountry(name):
    pelicula = {'name': "", "peliculas": None}
    pelicula['name'] = name
    pelicula['peliculas'] = lt.newList('SINGLE_LINKED', compare_companies_byname)
    return pelicula

def newCompanie(name):
    pelicula = {'name': "", "pelicula": None,  "vote_average": 0}
    pelicula['name'] = name
    pelicula['pelicula'] = lt.newList('SINGLE_LINKED', compare_companies_byname)
    return pelicula

# ==============================
# Funciones de consulta
# ==============================
def encontrar_compañia(compania,catalogo):
    companie=mp.get(catalogo["productora"],compania)
    return companie
def encontrar_genero(nombre_genero,catalogo):
    genero=mp.get(catalogo["genero"],nombre_genero)
    return genero
def conocer_pais(nombre_pais,catalogo):
    pais=mp.get(catalogo["pais"],nombre_pais)
    return pais
def conocer_actor(nombre_actor,catalogo):
    actor=mp.get(catalogo["actor"],nombre_actor)
    return actor
def conocer_director(nombre_director, catalogo):
    director = mp.get(catalogo["director"], nombre_director)
    return director
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
# Funciones de Comparacion \ufeff
# ==============================

def compareRecordIds(recordA, recordB):
    if int(recordA["\ufeffid"]) == int(recordB["\ufeffid"]):
        return 0
    elif int(recordA["\ufeffid"]) > int(recordB["\ufeffid"]):
        return 1
    return -1
def compareMapMovieIds(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1
def compare_companies_byname(keyname, company):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(company)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1