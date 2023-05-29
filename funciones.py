import json
import re
import csv

def leer_archivo(ruta:str)->list:
    '''
    La función leer_archivo lee un archivo json y lo devuelve como una lista.
    
    Parametro:
        ruta: de tipo string, es la ruta en donde se encuentra el archivo JSON a leer.
    
    Devuelve: una lista de tipo list que posee el contenido del archivo JSON.
    '''
    with open(ruta, 'r') as archivo:
        diccionario = json.load(archivo)
    return diccionario["jugadores"]

def obtener_nombre_posicion(jugadores:list)->list:
    '''
    La función obtener_nombre_posicion recibe una lista de jugadores y crea una nueva lista que contiene el nombre y la posición de cada jugador en el formato "{índice}. {nombre} - {posición}". El índice se incrementa en 1 para que comience desde 1 en lugar de 0. 
    
    Parámetro:  
        jugadores: de tipo list, representa una lista de jugadores.
    
    Devuelve: una lista de tipo list con los nombres y posiciones de los jugadores.
    '''
    nombre_posicion_jugador = []
    
    for indice in range(len(jugadores)):
        jugador = jugadores[indice]
        nombre = jugador["nombre"]
        posicion = jugador["posicion"]
        nombre_posicion_jugador.append("{0}. {1} - {2}".format(indice+1, nombre, posicion))
    return nombre_posicion_jugador

def mostrar_estadisticas_jugador(jugadores:list, indice_jugador:float)->dict:
    '''
    La función mostrar_estadisticas_jugador muestra las estadísticas de un jugador específico en base a su índice dentro de la lista de jugadores.
    
    Parámetros:
        jugadores: de tipo list, representa una lista de jugadores.
        indice_jugador: de tipo float, representa índice del jugador deseado.
    
    Devuelve: un diccionario de tipo dict con las estadísticas del jugador especificado o None si el índice está fuera de rango.
    '''
    if indice_jugador >= 0 and indice_jugador < len(jugadores):
        jugador = jugadores[indice_jugador-1]
        nombre = jugador["nombre"]
        posicion = jugador["posicion"]
        estadisticas = jugador["estadisticas"]
        
        estadistica_jugador = {
            "Nombre": nombre,
            "Posición": posicion,
            "Temporadas jugadas": estadisticas["temporadas"],
            "Puntos totales": estadisticas["puntos_totales"],
            "Promedio de puntos por partido": estadisticas["promedio_puntos_por_partido"],
            "Rebotes totales": estadisticas["rebotes_totales"],
            "Promedio de rebotes por partido": estadisticas["promedio_rebotes_por_partido"],
            "Asistencias totales": estadisticas["asistencias_totales"],
            "Promedio de asistencias por partido": estadisticas["promedio_asistencias_por_partido"],
            "Robos totales": estadisticas["robos_totales"],
            "Bloqueos totales": estadisticas["bloqueos_totales"],
            "Porcentaje de tiros de campo": estadisticas["porcentaje_tiros_de_campo"],
            "Porcentaje de tiros libres": estadisticas["porcentaje_tiros_libres"],
            "Porcentaje de tiros triples": estadisticas["porcentaje_tiros_triples"]
        }
        
        return estadistica_jugador
    else:
        return None

def exportar_csv(nombre_archivo: str, estadistica_jugador: list) -> bool:
    '''
    La función exportar_csv exporta una lista de estadísticas de jugador a un archivo CSV.
    
    Parámetros:
        nombre_archivo: de tipo str, representa el nombre del archivo CSV a crear o sobrescribir.
        estadistica_jugador: de tipo dic, representa la lista de estadísticas de jugador.
    
    Devuelve: un booleano define True si el archivo se guardó correctamente, False si ocurrió un error al guardar el archivo.
    '''
    archivo_guardado = False
    if estadistica_jugador:
        # Agregar la extensión .csv al nombre del archivo si no está presente
        if not nombre_archivo.endswith(".csv"):
            nombre_archivo += ".csv"
        
        with open(nombre_archivo, 'w', newline='') as archivo:
            writer = csv.writer(archivo)

            encabezados = estadistica_jugador[0].keys()
            writer.writerow(encabezados)

            for dato in estadistica_jugador:
                valores = dato.values()
                writer.writerow(valores)
            archivo_guardado = True

    if archivo_guardado:
        print("Se creó el archivo: {0}".format(nombre_archivo))
    else:
        print("Error al crear el archivo: {0}".format(nombre_archivo))

    return archivo_guardado

def buscar_jugador(jugadores:list, nombre:str)->list:
    '''
    La función buscar_jugador busca un jugador por su nombre (completo o por al menos las primera 4 letras de su nombre o apellido) en una lista de jugadores y devuelve una lista de logros del jugador encontrado. Si no se encuentra el jugador, retorna una lista vacía.

    Parámetros:
        jugadores: de tipo list, representa una lista de jugadores.
        nombre: de tipo str, representa el nombre del jugador a buscar.
        
    Retorno: Una lista de tipo list que representa los logros del jugador encontrado.
    '''
    logros = []
    nombre_completo = ""
    nombre = nombre.lower() 
    for jugador in jugadores:
        nombre_jugador = jugador["nombre"].lower()
        apellido_jugador = jugador["nombre"].split()[-1].lower()

        if nombre in nombre_jugador or nombre in apellido_jugador:
            logros = jugador["logros"]
            nombre_completo = jugador["nombre"]
            break
        elif nombre in nombre_jugador[:4] or nombre in apellido_jugador[:4]:
            logros = jugador["logros"]
            nombre_completo = jugador["nombre"]
            break
    if not logros:
        print("No se encontró al jugador: {0}".format(nombre))
    return logros, nombre_completo

def promedio_puntos_por_partido(jugadores:list, atributo:str):
    '''
    La función promedio_puntos_por_partido ordena la lista de jugadores por su promedio de puntos por partido de menor a mayor utilizando el ordenamiento burbuja. Luego, muestra por pantalla el promedio de puntos por partido de cada jugador del Dream Team.

    Parámetros:
        jugadores: de tipo list, representa una lista de jugadores.
        atributo: de tipo str, indica el atributo estadístico utilizado para ordenar la lista de jugadores.
    Retorna: no tiene retorno.
    
    Imprime por pantalla el promedio de puntos por partido de cada jugador del Dream Team.
    '''
    if not jugadores:
        print("La lista se encuentra vacía.")
        return

    flag_swap = True

    while flag_swap:
        flag_swap = False

        for indice in range(len(jugadores)-1):
            valor_a = jugadores[indice]["estadisticas"][atributo]
            valor_b = jugadores[indice + 1]["estadisticas"][atributo]

            if valor_a > valor_b:
                jugadores[indice], jugadores[indice + 1] = jugadores[indice + 1], jugadores[indice]
                flag_swap = True

    print("Promedio de puntos por partido de cada jugador:")
    for jugador in jugadores:
        nombre_jugador = jugador["nombre"]
        promedio_puntos = jugador["estadisticas"]["promedio_puntos_por_partido"]
        print(nombre_jugador + ":", promedio_puntos)

def verificar_salon_de_la_fama(jugadores:list, nombre:str)->bool:
    '''
    La función verificar_salon_de_la_fama busca un jugador por su nombre (completo o por al menos las primera 4 letras de su nombre o apellido) en la lista de jugadores y verifica si entre sus logros se encuentra haber sido incluido en el Salón de la Fama del Baloncesto. Devuelve True si el jugador se encuentra en el Salón de la Fama, y False en caso contrario.

    Parámetros:
        jugadores: de tipo list, representa una lista de jugadores.
        nombre: de tipo str que indica el nombre del jugador a buscar.

    Retorna: un booleano de tipo bool que define True si el jugador se encuentra en el Salón de la Fama, False en caso contrario.
    '''
    logros = []
    nombre_completo = ""
    nombre = nombre.lower()  # Convertir el nombre ingresado a minúsculas
    for jugador in jugadores:
        nombre_jugador = jugador["nombre"].lower()
        apellido_jugador = jugador["nombre"].split()[-1].lower()

        if nombre in nombre_jugador or nombre in apellido_jugador:
            logros = jugador["logros"]
            nombre_completo = jugador["nombre"]
            
        elif nombre in nombre_jugador[:4] or nombre in apellido_jugador[:4]:
            logros = jugador["logros"]
            nombre_completo = jugador["nombre"]
            
        for logro in logros:
                if "Salón de la Fama del Baloncesto" in logro:
                    return True
    return logro, nombre_completo

def obtener_jugador_maximo(jugadores:list, estadistica:str)->list:
    '''
    La función obtener_jugador_maximo recibe una lista de jugadores y una estadística específica y devuelve una lista con el nombre de los jugadores que tienen el valor máximo en esa estadística.
    
    Parámetros:
        jugadores: de tipo list, representa una lista de jugadores.
        estadistica: de tipo str que representa la estadística específica a evaluar.

    Retorna: una lista de tipo list de nombres de jugadores que tienen el valor máximo en la estadística especificada.
    '''
    max_valor = 0
    jugadores_maximos = []

    for jugador in jugadores:
        valor_estadistica = jugador["estadisticas"][estadistica]
        if valor_estadistica > max_valor:
            max_valor = valor_estadistica
            jugadores_maximos = [jugador["nombre"]]
        elif valor_estadistica == max_valor:
            jugadores_maximos.append(jugador["nombre"])

    return jugadores_maximos

def jugador_con_mas_logros(jugadores:list)->list:
    '''
    La función jugador_con_mas_logros recibe una lista de jugadores y devuelve una lista con los jugadores que tienen la mayor cantidad de logros.
    
    Parámetros:
        jugadores: de tipo list, representa una lista de jugadores.

    Retorna: una lista de tuplas que contienen el nombre, la posición y la cantidad máxima de logros de los jugadores con más logros. Si no se encuentran jugadores con logros, retorna None.
    '''
    jugadores_max_logros = []
    cantidad_logros_maxima = 0

    for jugador in jugadores:
        logros = jugador['logros']
        cantidad_logros = len(logros)
        if cantidad_logros > cantidad_logros_maxima:
            jugadores_max_logros = [jugador]
            cantidad_logros_maxima = cantidad_logros
        elif cantidad_logros == cantidad_logros_maxima:
            jugadores_max_logros.append(jugador)

    if jugadores_max_logros:
        resultados = []
        for jugador in jugadores_max_logros:
            nombre_jugador = jugador['nombre']
            posicion_jugador = jugador['posicion']
            cantidad_logros = cantidad_logros_maxima
            resultados.append((nombre_jugador, posicion_jugador, cantidad_logros))
        
        return resultados
    else:
        return None

def jugadores_destacados(jugadores:list, estadistica:str, valor:float)->list:
    '''
    La función jugadores_destacados recibe una lista de jugadores, una estadística y un valor límite ingresado por el usuario, y devuelve una lista con los nombres de los jugadores que superan el valor límite en la estadística especificada.
    
    Parámetros:
        jugadores: de tipo list, representa una lista de jugadores.
        estadistica: de tipo str, representa la estadística a evaluar. Puede ser "puntos", "rebotes", "asistencias", "tiros_libres" o "tiros_triples".
        valor: de tipo float, un valor numérico ingresado por el usuario que representa el límite para considerar a un jugador como destacado en la estadística.

    Retorna: una lista de tipo list con los nombres de los jugadores que superan el valor límite en la estadística especificada. Si no se encuentra ningún jugador destacado, imprime un mensaje
    '''
    jugadores_destacados = []
    
    for jugador in jugadores:
        if estadistica == "puntos" and jugador["estadisticas"]["promedio_puntos_por_partido"] > valor:
            jugadores_destacados.append(jugador["nombre"])
        elif estadistica == "rebotes" and jugador["estadisticas"]["promedio_rebotes_por_partido"] > valor:
            jugadores_destacados.append(jugador["nombre"])
        elif estadistica == "asistencias" and jugador["estadisticas"]["promedio_asistencias_por_partido"] > valor:
            jugadores_destacados.append(jugador["nombre"])
        elif estadistica == "tiros_libres" and jugador["estadisticas"]["porcentaje_tiros_libres"] > valor:
            jugadores_destacados.append(jugador["nombre"])
        elif estadistica == "tiros_triples" and jugador["estadisticas"]["porcentaje_tiros_triples"] > valor:
            jugadores_destacados.append(jugador["nombre"])
            
    if not jugadores_destacados:
        print("No se encontraron jugadores que superen el valor ingresado en la estadística especificada.")
    
    
    return jugadores_destacados

def calcular_promedio_puntos_sin_minimo(jugadores: list) -> float:
    '''
    La funcion calcular_promedio_puntos_sin_minimo calcula el promedio de puntos por partido de una lista de jugadores excluyendo el valor mínimo.

    Parámetros:
        jugadores: de tipo list, representa una lista de jugadores.

    Retorna: el promedio de tipo float de puntos por partido sin tener en cuenta el valor mínimo, o 0 si no hay jugadores.
    '''
    puntos_por_partido = [jugador["estadisticas"]["promedio_puntos_por_partido"] for jugador in jugadores]
    puntos_por_partido_sin_minimo = []
    suma = 0
    contador = 0

    for puntos in puntos_por_partido:
        if puntos < min_puntos or not puntos_por_partido_sin_minimo:
            min_puntos = puntos
        else:
            puntos_por_partido_sin_minimo.append(puntos)
            suma += puntos
            contador += 1

    if contador > 0:
        promedio = suma / contador
        return promedio
    else:
        return 0
def mostrar_jugadores_superior_porcentaje_tiros(jugadores, valor:float):
    '''
    Muestra los jugadores con un porcentaje de tiros de campo superior a un valor ingresado por el usuario.

    Parámetros:
        jugadores: de tipo list, representa una lista de jugadores.
        valor: de tipo float, ingresado por el usuario, representa el valor de referencia para comparar el porcentaje de tiros de campo.

    Retorna: None

    Imprime por consola los jugadores que ctienen un porcentaje de tiros de campo superior al valor dado, ordenados por su posición.
    '''
    jugadores_superiores = []
    for jugador in jugadores:
        porcentaje_tiros_campo = jugador["estadisticas"]["porcentaje_tiros_de_campo"]
        if porcentaje_tiros_campo > valor:
            jugadores_superiores.append(jugador)

    for indice_a in range(len(jugadores_superiores) - 1):
        for indice_b in range(len(jugadores_superiores) - indice_a - 1):
            if jugadores_superiores[indice_b]["posicion"] > jugadores_superiores[indice_b + 1]["posicion"]:
                jugadores_superiores[indice_b], jugadores_superiores[indice_b + 1] = jugadores_superiores[indice_b + 1], jugadores_superiores[indice_b]

    if jugadores_superiores:
        print("Jugadores con porcentaje de tiros de campo superior a", valor)
        for jugador in jugadores_superiores:
            print("Posicion: {0} - Nombre: {1} - Porcentaje tiros de campo: {2}".format(jugador["posicion"], jugador["nombre"], jugador["estadisticas"]["porcentaje_tiros_de_campo"]))
    else:
        print("No hay jugadores con porcentaje de tiros de campo superior a", valor)

