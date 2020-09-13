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
from time import process_time
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller
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




# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________



# ___________________________________________________
#  Menu principal
# ___________________________________________________
def printMenu():
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Cargar información en el catálogo")
    print("3- Consultar el número de películas cargadas")
    print("4- Imprimir primera y ultima pelicula")
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
        controller.loadMovies(moviesfile,cont)
        
        
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
      
    else:
        sys.exit(0)
sys.exit(0)