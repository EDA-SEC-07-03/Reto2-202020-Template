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
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
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


<<<<<<< HEAD
moviesfile = "AllMoviesDetailsCleaned.csv"
<<<<<<< HEAD
=======
moviesfile = "SmallMoviesDetailsCleaned.csv"
movies_casting= "MoviesCastingRaw-small.csv"
>>>>>>> 0c57cbc6be830e2f84caaa21f8c36ab04ff58b86

=======
moviesfile2 = "AllMoviesCastingRaw.csv"
>>>>>>> j.quirogar


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
<<<<<<< HEAD
<<<<<<< HEAD
=======
    print("6- Conocer actor")
>>>>>>> j.quirogar
=======
    print("7- Imprimir película por género")
    print("8- Imprimir película por país")
>>>>>>> 0c57cbc6be830e2f84caaa21f8c36ab04ff58b86
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
<<<<<<< HEAD
        print(controller.loadMovies(moviesfile,moviesfile2,cont))
=======
        controller.loadMovies(moviesfile,movies_casting,cont)
>>>>>>> 0c57cbc6be830e2f84caaa21f8c36ab04ff58b86
        tiempo2=process_time()
        total=tiempo2-tiempo1
        print(total, "segundos")
        
        
    elif int(inputs[0]) == 3:
        print("Cargando numero de peliculas ....")
        print (controller.numeros_peliculas(moviesfile,cont,model.compareRecordIds))
        
        

    elif int(inputs[0]) == 4:
        print("Cargando info primera y segunda pelicula ....")
        print("___________________________________________________")
        print("primera pelicula")
        print("nombre de la pelicula:   ", str(controller.datos_primera(model.obtener_primera_pelicula(cont),model.obtener_ultima_pelicula(cont))[0]))
        print("fecha de estreno:   ", str(controller.datos_primera(model.obtener_primera_pelicula(cont),model.obtener_ultima_pelicula(cont))[1]))
        print("promedio de la votacion:   ", str(controller.datos_primera(model.obtener_primera_pelicula(cont),model.obtener_ultima_pelicula(cont))[2]))
        print("idioma de la pelicula:   ", str(controller.datos_primera(model.obtener_primera_pelicula(cont),model.obtener_ultima_pelicula(cont))[3]))
    
        print("___________________________________________________")

        print("segunda pelicula:     ")
        print("nombre de la pelicula:   ", str(controller.datos_primera(model.obtener_primera_pelicula(cont),model.obtener_ultima_pelicula(cont))[4]))
        print("fecha de estreno:   ", str(controller.datos_primera(model.obtener_primera_pelicula(cont),model.obtener_ultima_pelicula(cont))[5]))
        print("promedio de la votacion:   ", str(controller.datos_primera(model.obtener_primera_pelicula(cont),model.obtener_ultima_pelicula(cont))[6]))
        print("idioma de la pelicula:   ", str(controller.datos_primera(model.obtener_primera_pelicula(cont),model.obtener_ultima_pelicula(cont))[7]))
    
    


    elif int(inputs[0]) == 5:
        productora_a_buscar = input(str(" digite compañía de producción: "))
        asd = controller.conocer_compañia(cont,productora_a_buscar)
        mapa= asd["value"]["pelicula"]
        total=lt.size(mapa)
        mapax= asd["value"]["vote_average"]
        print("-----------------------------------------------")
        for i in range(1,lt.size(mapa)+1):
            elemento=lt.getElement(mapa,i)
            print("peliculas producidas por la productora:   ", elemento["title"])
        
        print("-----------------------------------------------")

        print("total de peliculas", total)

        print("-----------------------------------------------")

        print("promedio de votos", mapax)

        print("-----------------------------------------------")

<<<<<<< HEAD


    elif int(inputs[0]) == 6:
        actor_interes = input("digite el actor a buscar: ")
        con = controller.conocer_actor(cont, actor_interes)
        pelis_6 = con["peliculas"]
        total_6 = lt.size(pelis_6)
        pelis_6x = me.getValue(pelis_6["vote_average"])
        print("-----------------------------------------------")
        for i in range(1,lt.size(pelis_6)+1):
            elemento=lt.getElement(pelis_6,i)
            print("peliculas en las que aparece el actor:   ", elemento["title"])
        print("-----------------------------------------------")

        print("total de peliculas", total_6)

        print("-----------------------------------------------")

        print("promedio de votos", pelis_6x)

        print("-----------------------------------------------")



=======
    elif int(inputs[0]) == 7:
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
            print(x,elem)
            x+=1
        print("______________________________________________")
        print("Género elegido:",generox)
        print("Total películas",lt.size(pelis1))
        print("Promedio del género",promedio)
        print("______________________________________________")



    elif int(inputs[0]) == 8:
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
            elem=lt.getElement(pelis2,i)
            print(x,elem["title"],"   ",elem["director"],"   ",elem["release_date"])
            x+=1
        print("______________________________________________")
        print("Peliculas de:",pais)
        print("Titulo  Director  Fecha lanzamiento")
        print("______________________________________________")
>>>>>>> 0c57cbc6be830e2f84caaa21f8c36ab04ff58b86
    else:
        sys.exit(0)
sys.exit(0)