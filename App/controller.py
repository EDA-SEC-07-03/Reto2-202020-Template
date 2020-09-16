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
def loadCSVFile (file,catalog):
    dialect = csv.excel()
    dialect.delimiter=";"
    with open( config.data_dir + file, encoding="utf-8") as csvfile:
        row = csv.DictReader(csvfile, dialect=dialect)
        for elemento in row: 
            model.addmovie(catalog,elemento)
            companies=[elemento["production_companies"]]
            for i in companies:
                model.addmovie_company(catalog,i,elemento)

def numeros_peliculas (file,catalog,cmpfunction):
    dialect = csv.excel()
    dialect.delimiter=";"
    x = 0
    with open( config.data_dir + file, encoding="utf-8") as csvfile:
        row = csv.DictReader(csvfile, dialect=dialect)
        for elemento in row: 
            x += 1
    return x
def datos_primera(datos1 , datos2  ):
    datos_entrega = model.datos_pelicula(datos1, datos2)
    return datos_entrega

def loadMovies(dire,catalog):
    loadCSVFile(dire,catalog)

xd=initCatalog()
loadCSVFile("AllMoviesDetailsCleaned.csv",xd)
asd=model.encontrar_compañia("Pixar Animation Studios",xd)
print(asd)


