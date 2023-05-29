import re
import json
from funciones import *



ruta_archivo = "Parcial\dt.json"  
jugadores = leer_archivo(ruta_archivo)


def generar_menu()->str:
    '''
    La funcion generar_menu imprime en pantalla el menú con las opciones disponibles del programa.

    Retorna: el menú de tipo str generado con las opciones enumeradas.
    '''
    menu = "1- {0}\n2- {1}\n3- {2}\n4- {3}\n5- {4}\n6- {5}\n7- {6}\n8- {7}\n9- {8}\n10- {9}\n11- {10}\n12- {11}\n13- {12}\n14- {13}\n15- {14}\n16- {15}\n17- {16}\n18- {17}\n19- {18}\n20- {19}\n21- {20}\n\n".format(
        "Mostrar la lista de todos los jugadores del Dream Team.",
        "Seleccionar un jugador por su índice y mostrar sus estadísticas completas",
        "Guardar las estadísticas de ese jugador en un archivo CSV",
        "Buscar un jugador por su nombre y mostrar sus logros",
        "Mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente",
        "Ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto",
        "Mostrar el jugador con la mayor cantidad de rebotes totales",
        "Mostrar el jugador con el mayor porcentaje de tiros de campo",
        "Mostrar el jugador con la mayor cantidad de asistencias totales",
        "Ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor",
        "Ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor",
        "Ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor",
        "Mostrar el jugador con la mayor cantidad de robos totales",
        "Mostrar el jugador con la mayor cantidad de bloqueos totales",
        "Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor",
        "Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido",
        "Mostrar el jugador con la mayor cantidad de logros obtenidos",
        "Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor",
        "Mostrar el jugador con la mayor cantidad de temporadas jugadas",
        "Ingresar un valor y mostrar los jugadores, ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor",
        # "Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking: Puntos, Rebotes, Asistencias y Robos",
        "Salir"
    )
    return menu
    
def validacion_respuesta_menu(respuesta: str) -> bool:
    '''
    La función validacion_respuesta_menu recibe una cadena de texto y devuelve un valor booleano que comprueba si la respuesta cumple con el patrón de un número del 1 al 9 o un número de dos dígitos del 10 al 21.
    
    Parámetros:
        respuesta: de tipo str, representa la respuesta proporcionada por el usuario.
    
    Retorna: True si la respuesta es válida y cumple con el patrón, False en caso contrario.    '''
    busqueda = re.match(r'^[1-9]|[1-2][0-1]$', respuesta)
    if busqueda:
        return True
    else:
        return False


def app_jugadores():
    '''
    La función app_jugadores es el punto de entrada principal de la aplicación de jugadores.
    Ejecuta un ciclo infinito que muestra el menú generado por la función generar_menu, lee la opción seleccionada por el usuario y realiza diferentes acciones según la opción elegida.
    Si la opción seleccionada es válida, el ciclo continúa. Si no es válida, se muestra un mensaje de error.
    La función app_jugadores termina cuando se selecciona la opción "Salir" en el menú.
    '''
    while True:
        print(generar_menu())  

        respuesta = input("Ingrese una opción: ")
        if validacion_respuesta_menu(respuesta):
            opcion = int(respuesta)            
            match(int(respuesta)):
                case 1:
                    resultado = obtener_nombre_posicion(jugadores)

                    for jugador in resultado:
                        print(jugador)
                case 2:
                    indice_jugador = int(input("Ingresa el índice del jugador deseado: "))
                    estadisticas_jugador = mostrar_estadisticas_jugador(jugadores, indice_jugador)
                    print(estadisticas_jugador)
                case 3:
                    nombre_archivo = "estadisticas_jugador.csv"
                    estadisticas_jugadores = [estadisticas_jugador] 
                    resultado = exportar_csv(nombre_archivo, estadisticas_jugadores)
                case 4:
                    nombre_jugador = input("Ingrese el nombre del jugador: ")
                    logros_jugador, nombre_completo_jugador = buscar_jugador(jugadores, nombre_jugador)

                    if logros_jugador:
                        print("Logros de", nombre_completo_jugador + ":")
                        for logro in logros_jugador:
                            print("-", logro)
                    else:
                        print("No se encontró el jugador", nombre_jugador)
                case 5:
                    atributo_orden = "promedio_puntos_por_partido"

                    promedio_puntos_por_partido(jugadores, atributo_orden)
                case 6:
                    nombre_jugador = input("Ingrese el nombre del jugador: ")
                    es_miembro_salon_fama, nombre_completo_jugador = verificar_salon_de_la_fama(jugadores, nombre_jugador)
                    if es_miembro_salon_fama:
                        print("{} es miembro del Salón de la Fama del Baloncesto.".format(nombre_completo_jugador))
                    else:
                        print("{} no es miembro del Salón de la Fama del Baloncesto.".format(nombre_completo_jugador))
                case 7:
                    jugador_max_rebotes = obtener_jugador_maximo(jugadores, "rebotes_totales")
                    print("Jugador con la mayor cantidad de rebotes totales:", jugador_max_rebotes)
                case 8:
                    jugador_max_porcentaje_tiros_campo = obtener_jugador_maximo(jugadores, "porcentaje_tiros_de_campo")
                    print("Jugador con el mayor porcentaje de tiros de campo:", jugador_max_porcentaje_tiros_campo)
                case 9:
                    jugador_max_asistencias = obtener_jugador_maximo(jugadores, "asistencias_totales")
                    print("Jugador con la mayor cantidad de asistencias totales:", jugador_max_asistencias)
                case 10:
                    valor_ingresado = float(input("Ingrese un valor: "))

                    jugadores_puntos_destacados = jugadores_destacados(jugadores, "puntos", valor_ingresado)
                    print("Jugadores con promedio de puntos por partido mayor a", valor_ingresado)
                    for jugador in jugadores_puntos_destacados:
                        print(jugador)
                case 11:
                    valor_ingresado = float(input("Ingrese un valor: "))
                    jugadores_rebotes_destacados = jugadores_destacados(jugadores, "rebotes", valor_ingresado)
                    print("Jugadores con promedio de rebotes por partido mayor a", valor_ingresado)
                    for jugador in jugadores_rebotes_destacados:
                        print(jugador)
                case 12:
                    valor_ingresado = float(input("Ingrese un valor: "))
                    jugadores_asistencias_destacados = jugadores_destacados(jugadores, "asistencias", valor_ingresado)
                    print("Jugadores con promedio de asistencias por partido mayor a", valor_ingresado)
                    for jugador in jugadores_asistencias_destacados:
                        print(jugador)
                case 13:
                    jugador_max_robos = obtener_jugador_maximo(jugadores, "robos_totales")
                    print("Jugador con la mayor cantidad de robos totales:", jugador_max_robos)
                case 14:
                    jugador_max_bloqueos = obtener_jugador_maximo(jugadores, "bloqueos_totales")
                    print("Jugador con la mayor cantidad de bloqueos totales:", jugador_max_bloqueos)
                case 15:
                    valor_tiros_libres = float(input("Ingrese un valor para el porcentaje de tiros libres: "))
                    jugadores_tiros_libres_destacados = jugadores_destacados(jugadores, "tiros_libres", valor_tiros_libres)
                    print("Jugadores con porcentaje de tiros libres superior a", valor_tiros_libres)
                    for jugador in jugadores_tiros_libres_destacados:
                        print(jugador)
                case 16:
                    promedio_puntos = calcular_promedio_puntos_sin_minimo(jugadores)
                    print("Promedio de puntos por partido del equipo (excluyendo al jugador con la menor cantidad de puntos por partido):", promedio_puntos)
                case 17:
                    resultado = jugador_con_mas_logros(jugadores)
                    if resultado:
                        nombre_jugador, posicion_jugador, cantidad_logros = resultado
                        print("Jugador con más logros:\n Nombre: {0} \n Posición: {1} \n Cantidad de logros: {2}".format(nombre_jugador, posicion_jugador, cantidad_logros))
                    else:
                        print("No se encontró ningún jugador con logros.")                
                case 18:
                    valor_tiros_triples = float(input("Ingrese un valor para el porcentaje de tiros triples: "))
                    jugadores_tiros_triples_destacados = jugadores_destacados(jugadores, "tiros_triples", valor_tiros_triples)
                    print("Jugadores con porcentaje de tiros triples superior a", valor_tiros_triples)
                    for jugador in jugadores_tiros_triples_destacados:
                        print(jugador)
                case 19:
                    jugador_max_temporadas = obtener_jugador_maximo(jugadores, "temporadas")
                    print("Jugador con la mayor cantidad de temporadas jugadas:", jugador_max_temporadas)
                case 20:
                    valor_tiros_campo = float(input("Ingrese un valor para el porcentaje de tiros de campo: "))
                    jugadores_tiros_campo_destacados = mostrar_jugadores_superior_porcentaje_tiros(jugadores, valor_tiros_campo)
                # case 21:
                #     resultado = calcular_obtener_posicion_ranking_jugadores(jugadores) 
                #     for jugador in resultado:
                #         print("Jugador: {0} - Posición en el ranking de puntos: {1} - Posición en el ranking de rebotes: {2} - Posición en el ranking de asistencias: {3} - Posición en el ranking de robos: {4}".format(jugador["nombre"], jugador["Puntos"], jugador["Rebotes"], jugador["Asistencias"], jugador["Robos"]))
                #     resultado_b = calcular_obtener_posicion_ranking_jugadores(jugadores)
                #     exportar_csv("ranking_jugadores.csv", resultado_b)
                case 21:
                    break

        else:
            print("Opción incorrecta, ingrese una opción nuevamente.")