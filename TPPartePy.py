# TP FINAL - PARTE PYTHON - Sebastian Giulianelli - legajo:(G-5739/8)

from os import system
from random import choice, randint


######################################## FUNCIONES GENERALES ################################################
#abrir_archivo: FILE -> Tuple
#             : La funcion recibe un archivo de texto y retorna una tupla de tres elementos, el primero es la dimension,
#             : el segundo es la lista de palabras y el tercero es la complejidad de la sopa.
def abrir_archivo(archivo):
    f = open(archivo, "r")
    texto = f.readlines()
    dimension = int(texto[1].strip())
    listaPalabras = []
    contador = 4
    while not(texto[contador] == "\n"):
        listaPalabras.append(texto[contador].strip())  
        contador += 1
    complejidad = int(texto[contador + 2].strip())
    f.close()
    return dimension, listaPalabras, complejidad

#----------------------------------------

#tablero_vacio: int -> list(list)
#             : La funcion crea un tablero segun una dimension tomada como parametro. Este tablero esta dado como
#             : una lista de listas de caracteres. En este caso los caracteres son siempre iguales.
def tablero_vacio(dimension):
    tablero = []
    for x in range(dimension):
        tablero += [list(dimension*".")]
    return tablero

#----------------------------------------

#agregar_palabra: list(list) string list list -> list(list)
#               : La funcion se encarga de agregar una palabra tomada como parametro en el tablero de la sopa, dandole una direccion y sentido
#               : segun su complejidad. Si no es posible agregar esta palabra al tablero, la funcion retorna 0.
def agregar_palabra(tablero, palabra, dimension, complejidad):
    largoPalabra = len(palabra)
    direccion = direccion_y_sentido(complejidad)[0]
    sentido = direccion_y_sentido(complejidad)[1]
    pXY = posicion_en_tablero(palabra, largoPalabra, tablero, direccion, sentido, complejidad, dimension)
    if pXY == 0:
        return 0
    pX = pXY[0]
    pY = pXY[1]
    tablero = colocar_palabra(pX, pY, palabra, largoPalabra, tablero, direccion, sentido)
    return tablero

#----------------------------------------

#crear_tablero: int list int list(list) -> list(list)
#             : La funcion, a partir de un tablero vacio, genera un tablero semi-vacio con las palabras ya agregadas. Si no fue posible crear este
#             : tablero, la funcion retorna 0.
def crear_tablero(dimension, listaPalabras, complejidad, tableroVacio):
    tablero = tableroVacio
    for palabra in listaPalabras:
        tablero = agregar_palabra(tablero, palabra, dimension, complejidad)
        if tablero == 0:
            return 0
    return tablero

#----------------------------------------

#rellenar_tablero: list(list) -> list(list)
#                : La funcion toma un tablero semi-vacio y lo rellena de letras aleatorias en los espacios vacios. Luego lo retorna.
def rellenar_tablero(tablero):
    contador1 = 0
    contador2 = 0
    for fila in tablero:
        for x in fila:
            if x == ".":
                tablero[contador1][contador2] = choice(alfabeto())
            contador2 += 1
        contador1 += 1
        contador2 = 0
    return tablero

#----------------------------------------

#mostrar_tablero: list(list) int int int -> None
#               : La funcion recibe un tablero completo y lo muestra en pantalla en forma de matriz.
def mostrar_tablero(tablero, dimension, complejidad, cantPalabras):
    print("\n--- SOPA DE LETRAS --- Dimension(" + str(dimension) + ") --- Palabras(" + str(cantPalabras) + ") --- Complejidad(" + str(complejidad) +  ") ---\n\n")
    for x in tablero:
        for y in x:
            print(y.upper(),end = 2*" ")
        print("\n")
    print("\n\n")
##################################################################################################################


########################################### FUNCIONES AUXILIARES ###################################################
#albabeto: None -> String
#        : La funcion retorna un string del abecedario
def alfabeto():
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#----------------------------------------

#direccion_y_sentido: int -> tuple
#                   : La funcion recibe la complejidad de la sopa de letras y devuelve una tupla (direccion, sentido) para 
#                   : alguna palabra cualquiera.
#                   : Direccion = 1 -> Horizontal
#                   : Direccion = 2 -> Vertical
#                   : Direccion = 3 -> Diagonal(\)
#                   : Direccion = 4 -> Diagonal(/) 
#                   : Sentido = 1 -> Izquierda a derecha
#                   : Sentido = 2 -> Derecha a izquierda
def direccion_y_sentido(complejidad):
    if complejidad == 0:
        return randint(1,2), 1
    elif complejidad == 1:
        return randint(1,3), 1
    else:
        return randint(1,4), randint(1,2)

#----------------------------------------

#con_choque_no_valido: int int int list(list) int int -> Boolean
#                : La funcion determina si una palabra en una direccion y sentido establecido, es posible ubicarla en una
#                : posicion determinada y en un tablero semi-vacio dado sin que choque ninguna letra.
def con_choque_no_valido(pX, pY, largoPalabra, tablero, direccion, sentido):
    if direccion == 1:
        if sentido == 1:
            for x in range(largoPalabra):
                if tablero[pY][pX + x] != ".":
                    return True
        else:
            for x in range(largoPalabra):
                if tablero[pY][pX - x] != ".":
                    return True
    elif direccion == 2:
        if sentido == 1:
            for x in range(largoPalabra):
                if tablero[pY + x][pX] != ".":
                        return True
        else:
            for x in range(largoPalabra):
                if tablero[pY - x][pX] != ".":
                        return True
    elif direccion == 3:
        if sentido == 1:
            for x in range(largoPalabra):
                if tablero[pY + x][pX + x] != ".":
                        return True
        else:
            for x in range(largoPalabra):
                if tablero[pY - x][pX - x] != ".":
                        return True
    elif direccion == 4:
        if sentido == 1:
            for x in range(largoPalabra):
                if tablero[pY - x][pX + x] != ".":
                        return True
        else:
            for x in range(largoPalabra):    
                if tablero[pY + x][pX - x] != ".":
                        return True
    return False

#----------------------------------------

#con_choque_valido: int int string int list(list) int int -> Boolean
#                : La funcion determina si una palabra en una direccion y sentido establecido, es posible ubicarla en una
#                : posicion determinada y en un tablero semi-vacio dado sin que choque ninguna letra que no coincida con la de la palabra.
def con_choque_valido(pX, pY, palabra, largoPalabra, tablero, direccion, sentido):
    if direccion == 1:
        if sentido == 1:
            for x in range(largoPalabra):
                if tablero[pY][pX + x] != "." and tablero[pY][pX + x] != palabra[x]:
                    return True
        else:
            for x in range(largoPalabra):
                if tablero[pY][pX - x] != "." and tablero[pY][pX - x] != palabra[x]:
                    return True
    elif direccion == 2:
        if sentido == 1:
            for x in range(largoPalabra):
                if tablero[pY + x][pX] != "." and tablero[pY + x][pX] != palabra[x]:
                        return True
        else:
            for x in range(largoPalabra):
                if tablero[pY - x][pX] != "." and tablero[pY - x][pX] != palabra[x]:
                        return True
    elif direccion == 3:
        if sentido == 1:
            for x in range(largoPalabra):
                if tablero[pY + x][pX + x] != "." and tablero[pY + x][pX + x] != palabra[x]:
                        return True
        else:
            for x in range(largoPalabra):
                if tablero[pY - x][pX - x] != "." and tablero[pY - x][pX - x] != palabra[x]:
                        return True
    elif direccion == 4:
        if sentido == 1:
            for x in range(largoPalabra):
                if tablero[pY - x][pX + x] != "." and tablero[pY - x][pX + x] != palabra[x]:
                        return True
        else:
            for x in range(largoPalabra):    
                if tablero[pY + x][pX - x] != "." and tablero[pY + x][pX - x] != palabra[x]:
                        return True
    return False

#----------------------------------------

#calcular_posicion: int int int int list(list) int string int int int -> tuple | int
#                 : La funcion toma un rango de lugares posibles en el tablero para el inicio de una palabra y devuelve una posicion aleatoria
#                 : valida donde colocar la palabra segun la direccion, sentido y complejidad dada. Si no existe ninguna posicion posible 
#                 : para la palabra(esto se verifica viendo si la cant de coordenadas posibles es igual al tamaño de la lista de coordenadas no 
#                 : validas), la funcion retorna 0.
def calcular_posicion(minX, maxX, minY, maxY, tablero, complejidad, palabra, largoPalabra, direccion, sentido):
    posicionesNoValidas = []
    pXY = (randint(minX, maxX), randint(minY, maxY))
    if complejidad != 3:
        while con_choque_no_valido(pXY[0], pXY[1], largoPalabra, tablero, direccion, sentido):
            posicionesNoValidas.append(pXY)
            if len(posicionesNoValidas) == (maxX - (minX - 1)) * (maxY - (minY - 1)):
                return 0
            pXY = random(minX, maxX, minY, maxY, posicionesNoValidas)
        return pXY[0], pXY[1]
    else:
        while con_choque_valido(pXY[0], pXY[1], palabra, largoPalabra, tablero, direccion, sentido):
            posicionesNoValidas.append(pXY)
            if len(posicionesNoValidas) == (maxX - (minX - 1)) * (maxY - (minY - 1)):
                return 0
            pXY = random(minX, maxX, minY, maxY, posicionesNoValidas)
        return pXY[0], pXY[1]

#----------------------------------------

#posicion_en_tablero: string int list(list) int int int int -> tuple | int
#                   : La funcion calcula con ayuda de la funcion calcular_posicion(1) una posicion valida para colocar la palabra, esto lo
#                   : hace pasandole las coordenadas minimas y maximas a (1). Si no es posible encontrar ninguna posicion la funcion retorna 0.
def posicion_en_tablero(palabra, largoPalabra, tablero, direccion, sentido, complejidad, dimension):
    if direccion == 1:
        if sentido == 1:
            pXY = calcular_posicion(0, dimension-largoPalabra, 0, dimension-1, tablero, complejidad, palabra, largoPalabra, direccion, sentido)
            if pXY == 0:
                return 0
            pX = pXY[0]
            pY = pXY[1]
            return pX, pY
        else:
            pXY = calcular_posicion(largoPalabra-1, dimension-1, 0, dimension-1, tablero, complejidad, palabra, largoPalabra, direccion, sentido)
            if pXY == 0:
                return 0
            pX = pXY[0]
            pY = pXY[1]
            return pX, pY
    elif direccion == 2:
        if sentido == 1:
            pXY = calcular_posicion(0, dimension-1, 0, dimension-largoPalabra, tablero, complejidad, palabra, largoPalabra, direccion, sentido)
            if pXY == 0:
                return 0
            pX = pXY[0]
            pY = pXY[1]
            return pX, pY
        else:
            pXY = calcular_posicion(0, dimension-1, largoPalabra-1, dimension-1, tablero, complejidad, palabra, largoPalabra, direccion, sentido)
            if pXY == 0:
                return 0
            pX = pXY[0]
            pY = pXY[1]
            return pX, pY
    elif direccion == 3:
        if sentido == 1:
            pXY = calcular_posicion(0, dimension-largoPalabra, 0, dimension-largoPalabra, tablero, complejidad, palabra, largoPalabra, direccion, sentido)
            if pXY == 0:
                return 0
            pX = pXY[0]
            pY = pXY[1]
            return pX, pY
        else:
            pXY = calcular_posicion(largoPalabra-1, dimension-1, largoPalabra-1, dimension-1, tablero, complejidad, palabra, largoPalabra, direccion, sentido)
            if pXY == 0:
                return 0
            pX = pXY[0]
            pY = pXY[1]
            return pX, pY
    else:
        if sentido == 1:
            pXY = calcular_posicion(0, dimension-largoPalabra, largoPalabra-1, dimension-1, tablero, complejidad, palabra, largoPalabra, direccion, sentido)
            if pXY == 0:
                return 0
            pX = pXY[0]
            pY = pXY[1]
            return pX, pY
        else:
            pXY = calcular_posicion(largoPalabra-1, dimension-1, 0, dimension-largoPalabra, tablero, complejidad, palabra, largoPalabra, direccion, sentido)
            if pXY == 0:
                return 0
            pX = pXY[0]
            pY = pXY[1]
            return pX, pY

#----------------------------------------

#colocar_palabra: int int string int list(list) int int -> list(list)
#               : La funcion, una vez calculada la posicion de la palabra, carga la misma en el tablero segun la direccion y sentido de esta. Una
#               : vez hecho, retorna el tablero actualizado.
def colocar_palabra(pX, pY, palabra, largoPalabra, tablero, direccion, sentido):
    if direccion == 1:
        if sentido == 1:
            for x in range(largoPalabra):
                    tablero[pY][pX + x] = palabra[x]
        else:
            for x in range(largoPalabra):
                    tablero[pY][pX - x] = palabra[x]
    elif direccion == 2:
        if sentido == 1:
            for x in range(largoPalabra):
                    tablero[pY + x][pX] = palabra[x]
        else:
            for x in range(largoPalabra):
                    tablero[pY - x][pX] = palabra[x]
    elif direccion == 3:
        if sentido == 1:
            for x in range(largoPalabra):
                    tablero[pY + x][pX + x] = palabra[x]
        else:
            for x in range(largoPalabra):
                    tablero[pY - x][pX - x] = palabra[x]
    else:
        if sentido == 1:
            for x in range(largoPalabra):
                    tablero[pY - x][pX + x] = palabra[x]
        else:
            for x in range(largoPalabra):
                    tablero[pY + x][pX - x] = palabra[x]
    return tablero

#----------------------------------------

#random: int int int  int list -> tuple
#      : La funcion toma dos rangos, uno para X y uno para Y, y una lista. Lo que hace es calcular una coordenada aleatoria entre estos rangos
#      : teniendo en cuenta que cualquiera sea esta, no puede estar en la lista tomada como parametro.  
def random(minX, maxX, minY, maxY, lista):
    random = (randint(minX, maxX), randint(minY, maxY))
    while random in lista:
        random = (randint(minX, maxX), randint(minY, maxY))
    return random
##################################################################################################################


########################################## FUNCIONES DE VERIFICACION ##########################################################
#contar_letras: list -> int
#             : La funcion cuenta la cantidad de letras que hay en una lista de palabras.
def contar_letras(listaPalabras):
    cantidadTotal = 0
    for palabra in listaPalabras:
        cantidadTotal += len(palabra)
    return cantidadTotal

#----------------------------------------

#largo_maximo: list -> int
#            : La funcion devuelve el tamaño de la palabra mas larga de la lista.
def largo_maximo(listaPalabras):
    largoMaximo = 0
    for palabra in listaPalabras:
        if largoMaximo < len(palabra):
            largoMaximo = len(palabra)
    return largoMaximo

#----------------------------------------

#se_repiten: list(list) list int -> Boolean
#          : La funcion toma una lista de palabras y un tablero y verifica que no se repita mas de una vez cualquier palabra de la lista. Si esto 
#          : sucede, la funcion retorna True, caso contrario, False
def se_repiten(tableroCompleto, listaPalabras, dimension):
    contador = 0
    cy = 0
    cx = 0
    for palabra in listaPalabras:
        for fila in tableroCompleto:
            for letra in fila:
                if letra == palabra[0]:
                    contador += horizontal(cx, cy, tableroCompleto, palabra, dimension) + vertical(cx, cy, tableroCompleto, palabra, dimension) + diagonales(cx, cy, tableroCompleto, palabra, dimension)  
                if contador > 1:
                    return True
                cx += 1
            cy += 1
            cx = 0
        cx = 0
        cy = 0
        contador = 0
    return False    

#----------------------------------------

#horizontal: int int list(list) string int -> int
#          : La funcion se fija si existe la palabra tomada como parametro en una posicion del tablero en direccion horizontal y en sentido normal e inverso,
#          : y devuelve la cantidad de palabras que encuentre.
def horizontal(x, y, tableroCompleto, palabra, dimension):
    contadorDePalabras = 2
    contador = 0
    #izquierda a derecha
    for letra in palabra:
        if (x + contador >= dimension):
            contadorDePalabras -= 1
            break
        elif (letra != tableroCompleto[y][x + contador]) : 
            contadorDePalabras -= 1
            break
        contador += 1
    
    contador = 0
    #derecha a izquierda
    for letra in palabra:
        if  (x - contador < 0):
            contadorDePalabras -= 1
            break
        elif (letra != tableroCompleto[y][x - contador]): 
            contadorDePalabras -= 1
            break
        contador += 1
    return contadorDePalabras

#---------------------------------------- 

#vertical: int int list(list) string int -> int
#          : La funcion se fija si existe la palabra tomada como parametro en una posicion del tablero en direccion vertical y en sentido normal e inverso,
#          : y devuelve la cantidad de palabras que encuentre.
def vertical(x, y, tableroCompleto, palabra, dimension):
    contadorDePalabras = 2
    contador = 0
    #arriba a abajo
    for letra in palabra:
        if (y + contador >= dimension):
            contadorDePalabras -= 1
            break
        elif (letra != tableroCompleto[y + contador][x]): 
            contadorDePalabras -= 1
            break
        contador += 1
    
    contador = 0
    #abajo a arriba
    for letra in palabra:
        if  (y - contador < 0):
            contadorDePalabras -= 1
            break
        elif (letra != tableroCompleto[y - contador][x]): 
            contadorDePalabras -= 1
            break
        contador += 1
    return contadorDePalabras

#----------------------------------------

#diagonales: int int list(list) string int -> int
#          : La funcion se fija si existe la palabra tomada como parametro en una posicion del tablero en las direcciones diagonales y en sentido normal e inverso,
#          : y devuelve la cantidad de palabras que encuentre.
def diagonales(x, y, tableroCompleto, palabra, dimension):
    contadorDePalabras = 4
    contador = 0
    #arriba(izq) a abajo(der)
    for letra in palabra:
        if (y + contador >= dimension):
            contadorDePalabras -= 1
            break
        elif (x + contador >= dimension):
            contadorDePalabras -= 1
            break 
        elif (letra != tableroCompleto[y + contador][x + contador]): 
            contadorDePalabras -= 1
            break
        contador += 1
    
    contador = 0
    #abajo(der) a arriba(izq)
    for letra in palabra:
        if  (y - contador < 0):
            contadorDePalabras -= 1
            break 
        elif (x - contador < 0):
            contadorDePalabras -= 1
            break 
        elif (letra != tableroCompleto[y - contador][x - contador]): 
            contadorDePalabras -= 1
            break
        contador += 1
    
    contador = 0
    #abajo(izq) a arriba(der)
    for letra in palabra:
        if (y - contador < 0):
            contadorDePalabras -= 1
            break 
        elif (x + contador >= dimension):
            contadorDePalabras -= 1
            break 
        elif (letra != tableroCompleto[y - contador][x + contador]):
            contadorDePalabras -= 1
            break
        contador += 1

    contador = 0
    #arriba(der) a abajo(izq)
    for letra in palabra:
        if (y + contador >= dimension):
            contadorDePalabras -= 1
            break 
        elif (x - contador < 0):
            contadorDePalabras -= 1
            break 
        elif (letra != tableroCompleto[y + contador][x - contador]):
            contadorDePalabras -= 1
            break
        contador += 1
        
    return contadorDePalabras
##################################################################################################################


#main: None -> int
#    : La funcion principal lee un archivo de entrada y evalua 2 condiciones para generar la sopa.
#    : Si alguna de las palabras del archivo supera en largo a la dimension de la sopa o si la cantidad
#    : de letras total de todas las palabras(con una sopa de nivel 0, 1 o 2)  tiene mas letras que la sopa casillas, 
#    : la sopa no se puede generar y se muestra en un cartel. Si el archivo cumple con estas condiciones
#    : entonces se empieza a generar la sopa con un while de intentos. Si el while alcanza una cantidad 
#    : maxima determinada de ciclos y el tablero no se pudo generar, la funcion termina con un cartel
#    : que muestra esto. Si el tablero se pudo generar pasa a una instancia de relleno.
#    : Nuevamente, mediante un while de intentos maximos se va tratando de rellenar el tablero de modo
#    : que ninguna palabra se repita de casualidad dos veces. Si esto pasa y supera una cantidad
#    : de intentos, la funcion termina y muestra un cartel diciendo esto. 
#    : Si todas las condiciones son superadas, la funcion devuelve la sopa de letras generada.
def main():
    intentosMaximosSopa = 100000
    intentosMaximosRelleno = 10

    limpiar = "clear" #Linux
    system(limpiar)
    archivoAbrir = input("Ingrese el nombre del archivo a abrir: ")
    tupla = abrir_archivo(archivoAbrir)
    dimension = tupla[0]
    listaPalabras = tupla[1]
    complejidad = tupla[2]
    cantidadLetras = contar_letras(listaPalabras)

    if (cantidadLetras > dimension**2 and complejidad < 3) or (largo_maximo(listaPalabras) > dimension):
        print("No se puede generar esta sopa. La dimension dada no es suficiente.\n\n")
        return 0

    system(limpiar)
    print("Cargando...")
    tableroInicial = crear_tablero(dimension, listaPalabras, complejidad, tablero_vacio(dimension))

    c1 = 0
    while tableroInicial == 0 and c1 <= intentosMaximosSopa:
        tableroInicial = crear_tablero(dimension, listaPalabras, complejidad, tablero_vacio(dimension))
        c1 += 1

    if tableroInicial != 0:
        c2 = 0
        tableroCompleto = rellenar_tablero(tableroInicial)
        while se_repiten(tableroCompleto, listaPalabras, dimension) and c2 <= intentosMaximosRelleno:
            tableroCompleto = rellenar_tablero(tableroInicial)
            c2 += 1
    else:
        system(limpiar)
        print("No se puede generar esta sopa. Se alcanzo el maximo de intentos.\n\n")
        return 0

    if c2 > intentosMaximosRelleno:
        system(limpiar)
        print("No se puede generar esta sopa. \n\n")
        return 0 
    
    system(limpiar)
    mostrar_tablero(tableroCompleto, dimension, complejidad, len(listaPalabras))
    return 0

main()
