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

import sys
import config
import model
from DISClib.ADT import list as lt
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import listiterator as it
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as mp
from App import controller
from time import process_time 
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________


moviesfile = "AllMoviesDetailsCleaned.csv"
movies_casting= "AllMoviesCastingRaw.csv"



# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Cargar información en el catálogo")
    print("3- Consultar el número de películas cargadas")
    print("4- Imprimir primera y ultima pelicula")
    print("5- Descubrir productoras de cine")
    print("6- Conocer actor")
    print("7- Conocer director")
    print("8- Imprimir película por género")
    print("9- Imprimir película por país")
    print("0- Salir")

    
"""
Menu principal
"""



while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.initCatalog()

    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        tiempo1=process_time()
        controller.loadMovies(moviesfile,movies_casting,cont)
        tiempo2=process_time()
        total=tiempo2-tiempo1
        print(total, "segundos")
        
        
    elif int(inputs[0]) == 3:
        print("Cargando numero de peliculas ....")
        print(mp.size(cont["ids"]),mp.size(cont["casting"]))
        
    elif int(inputs[0]) == 4:
        print("obteniendo primera y última película")
        datosprimera=me.getValue(controller.datos_primera(cont))
        datosultima=me.getValue(controller.datos_ultima(cont))
        print("primera película")
        print("titulo:",datosprimera["title"])
        print("datos última")
        print("titulo:",datosultima["title"])
    elif int(inputs[0]) == 5:
        productora_a_buscar = input(str(" digite compañía de producción: "))
        asd = controller.conocer_compañia(cont,productora_a_buscar)
        mapa= me.getValue(asd)
        total=lt.size(mapa)
        mapax= me.getValue
        print("-----------------------------------------------")
        for i in range(1,lt.size(mapa)+1):
            elemento=lt.getElement(mapa,i)
            print("peliculas producidas por la productora:   ", elemento["title"])
        
        print("-----------------------------------------------")

        print("total de peliculas", total)

        print("-----------------------------------------------")

        print("promedio de votos", mapax)

        print("-----------------------------------------------")
    elif int(inputs[0]) == 6:
        actor_interes = input("digite el actor a buscar: ")
        con = controller.conocer_actor(cont, actor_interes)
        directores=con["directores"]
        peliculas=con["pelicula"]
        print("Directores con más colaboraciones")
        for i in range(1,lt.size(directores)+1):
            xd=lt.getElement(directores,i)
            print(xd)
        ow=1
        print("peliculas,N° peliculas:",lt.size(peliculas))
        for i in range(1,lt.size(peliculas)+1):
            xd=lt.getElement(peliculas,i)
            print(ow,xd["title"])
            ow+=1
        print("promedio")
        print(con["vote_average"])

        
    elif int(inputs[0]) == 7:
        director = input("digite el nombre del director a conocer: ")
        con_1 = controller.conocer_director(cont, director)
        con_1 = me.getValue(con_1)
        promedio_1 = con_1["vote_average"]
        peliculas_1 = con_1["pelicula"]
        y = 1
        print("______________________________________________")
        print("Peliculas de:",director)
        print("Titulo")
        print("______________________________________________")
        for i in range(1, lt.size(peliculas_1)+1):
            element = lt.getElement(peliculas_1, i)
            print(y, element["title"])
            y += 1
        print("______________________________________________")
        print("total de peliculas: ", y-1)
        print("promedio de peliculas: ", promedio_1)
        print("______________________________________________")
        print("Peliculas de:",director)

    elif int(inputs[0]) == 8:
        generox=input("Digite su género a buscar:\n")
        pelis=controller.conocer_genero(cont,generox)
        pelisx=me.getValue(pelis)
        pelis1=pelisx["pelicula"]
        promedio=pelisx["vote_average"]
        print("______________________________________________")
        print("Género elegido:",generox)
        print("Total películas",lt.size(pelis1))
        print("Promedio del género",promedio)
        print("______________________________________________")
        x=1
        for i in range(1,lt.size(pelis1)+1):
            elem=lt.getElement(pelis1,i)
            print(x,elem["title"])
            x+=1
        print("______________________________________________")
        print("Género elegido:",generox)
        print("Total películas",lt.size(pelis1))
        print("Promedio del género",promedio)
        print("______________________________________________")
    elif int(inputs[0]) == 9:
        pais=input("Pais a buscar:\n")
        pelis=controller.conocer_pais(cont,pais)
        pelis=me.getValue(pelis)
        pelis2=pelis["peliculas"]
        print("______________________________________________")
        print("Peliculas de:",pais)
        print("Titulo  Director  Fecha lanzamiento")
        print("______________________________________________")
        x=1
        for i in range(1,lt.size(pelis2)+1):
            elemento=lt.getElement(pelis2,i)
            print(x,elemento["title"],"  ",elemento["director"],"  ",elemento["release_date"])
            x+=1
        print("______________________________________________")
        print("Peliculas de:",pais)
        print("Titulo  Director  Fecha lanzamiento")
        print("______________________________________________")
    

    else:
        sys.exit(0)
sys.exit(0)


