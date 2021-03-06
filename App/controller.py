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
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from time import process_time
import model 
import csv
assert config


"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model.newCatalog()
    return catalog

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def loadCSVFileMovies (file,catalog):
    dialect = csv.excel()
    dialect.delimiter=";"
    with open( config.data_dir + file, encoding="utf-8") as csvfile:
        row = csv.DictReader(csvfile, dialect=dialect)
        for elemento in row: 
            model.addmovie(catalog,elemento)
            companies=[elemento["production_companies"]]
            genero=elemento["genres"].split("|")
            paises=[elemento["production_countries"]]
            for cm in companies:
                model.addmovie_company(catalog,cm,elemento)
            for gn in  genero:
                model.addmovie_genre(catalog,gn,elemento)
            for ps in paises:
                model.addmovie_pais(catalog,ps,elemento)

def loadCSVFileCasting(file,catalog):
    dialect = csv.excel()
    dialect.delimiter=";"
    with open( config.data_dir + file, encoding="utf-8") as csvfile:
        row = csv.DictReader(csvfile, dialect=dialect)
        for elemento in row: 
            model.addcasting(catalog,elemento)
            
def loadCSVFileCastingActor(file,catalog):
    dialect = csv.excel()
    dialect.delimiter=";"
    with open( config.data_dir + file, encoding="utf-8") as csvfile:
        row = csv.DictReader(csvfile, dialect=dialect)
        for elemento in row: 
           actores = [elemento["actor1_name"],elemento["actor2_name"],elemento["actor3_name"],elemento["actor4_name"],elemento["actor5_name"]]
           directores = [elemento["director_name"]]
           for act in actores:
               model.addmovie_actor(catalog, act, elemento)
           for dic in directores:
               model.addmovie_director(catalog, dic, elemento)

def numeros_peliculas (file,catalog,cmpfunction):
    dialect = csv.excel()
    dialect.delimiter=";"
    with open( config.data_dir + file, encoding="utf-8") as csvfile:
        row = csv.DictReader(csvfile, dialect=dialect)
        for elemento in row: 
           actores = [elemento["actor1_name"],elemento["actor2_name"],elemento["actor3_name"],elemento["actor4_name"],elemento["actor5_name"]]
           for act in actores:
               model.addmovie_actor(catalog, act, elemento)

def datos_primera(catalogo):
    datos=model.obtener_primera_pelicula(catalogo)
    return datos
def datos_ultima(catalogo):
    datos=model.obtener_ultima_pelicula(catalogo)
    return datos

def loadMovies(dire1,dire2,catalog):
    loadCSVFileCasting(dire2,catalog)
    loadCSVFileMovies(dire1,catalog)
    loadCSVFileCastingActor(dire2, catalog)
    
def conocer_compañia(catalog, compañia):
    x = model.encontrar_compañia(compañia, catalog)
    return x
def conocer_director(catalog, nombre_director):
    x = model.conocer_director(nombre_director, catalog)
    return x
def conocer_genero(catalog,genero):
    x= model.encontrar_genero(genero,catalog)
    return x
def conocer_pais(catalog,pais):
    xd=model.conocer_pais(pais,catalog)
    return xd
def conocer_actor(catalog,actor):
    x=model.conocer_actor(actor,catalog)
    llave_valor=me.getValue(x)
    director_mas_collab=llave_valor["directores"]
    valores=mp.valueSet(director_mas_collab)
    directores=mp.keySet(director_mas_collab)
    mas_colaboradores=lt.newList("ARRAY_LIST")
    mayor=0
    for i in range (1,lt.size(valores)):
        valor_director=lt.getElement(valores,i)
        if(valor_director >= mayor):
            mayor=valor_director
    for i in range (1,lt.size(directores)):
        director=lt.getElement(directores,i)
        if me.getValue(mp.get(director_mas_collab,director)) == mayor:
            lt.addLast(mas_colaboradores,director)
    llave_valor["directores"]=mas_colaboradores
    return llave_valor
    



            
