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
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria
"""

# -----------------------------------------------------
# API del TAD Catalogo de peliculas
# -----------------------------------------------------

def newCatalog():

    catalog = {'movies': None,
               'ids': None,
               "movies_name":None
               }

    catalog['movies'] = lt.newList('SINGLE_LINKED',)
    catalog['ids'] = mp.newMap(325001,
                                   maptype='PROBING',
                                   loadfactor=1.0,
                                   comparefunction=compare_movies)

    catalog['movies_name'] = mp.newMap(325001,
                                   maptype='PROBING',
                                   loadfactor=1.0,
                                   comparefunction=compare_movies)
    
    return catalog

# Funciones para agregar informacion al catalogo



# ==============================
# Funciones de consulta
# ==============================



# ==============================
# Funciones de Comparacion
# ==============================

def compare_movies(pos1,pos2):
    if(pos1 == pos2):
        return 0
    if(pos1 > pos2):
        return 1
    else:
        return -1
