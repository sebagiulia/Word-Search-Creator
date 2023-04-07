from TPPartePy import *

############################################# TESTS FUNCIONES PARTE PYTHON ##########################################################

def test_tablero_vacio():
    assert tablero_vacio(1) == [["."]]
    assert tablero_vacio(3) == [[".",".","."],[".",".","."],[".",".","."]]

#--------------------------------------------------------------------------------------

def test_con_choque_no_valido():
    tablero = [["s",".","."],["o",".","."],["l",".","."]]
    assert con_choque_no_valido(0, 2, 3, tablero, 1, 1) == True
    assert con_choque_no_valido(1, 0, 3, tablero, 2, 1) == False

#--------------------------------------------------------------------------------------

def test_con_choque_valido():
    tablero = [["s",".","."],[".","o","."],[".",".","l"]]
    assert con_choque_valido(2, 0, "gol", 3, tablero, 2, 1) == False
    assert con_choque_valido(0, 2, "gol", 3, tablero, 4, 1) == False
    assert con_choque_valido(0, 0, "gol", 3, tablero, 2, 1) == True

#--------------------------------------------------------------------------------------

def test_colocar_palabra():
    tableroInicial1 = [[".",".","."],[".",".","."],[".",".","."]]
    tableroFinal1 = [["s",".","."],[".","o","."],[".",".","l"]]
    assert colocar_palabra(0, 0, "sol", 3, tableroInicial1, 3, 1) == tableroFinal1
    tableroInicial2 = [[".","g","."],[".","o","."],[".","l","."]]
    tableroFinal2 = [[".","g","."],["l","o","s"],[".","l","."]]
    assert colocar_palabra(2, 1, "sol", 3, tableroInicial2, 1, 2) == tableroFinal2

#--------------------------------------------------------------------------------------

def test_contar_letras():
    listaPalabras1 = ["hola"]
    listaPalabras2 = ["hola", "cha", "u"]
    assert contar_letras(listaPalabras1) == 4
    assert contar_letras(listaPalabras2) == 8 

#--------------------------------------------------------------------------------------

def test_largo_maximo():
    lista1 = ["hola", "chau", "adios"]
    lista2 = ["minimos", "maximos", "iguales"]
    assert largo_maximo(lista1) == 5
    assert largo_maximo(lista2) == 7

#--------------------------------------------------------------------------------------

def test_se_repiten():
    lista = ["sol"]
    sopa1 = [["s","o","l"],["t","e","o"],["p","q","s"]]
    sopa2 = [["s","o","s"],["t","o","o"],["p","q","l"]]
    sopa3 = [["s","o","l"],["t","e","u"],["p","q","s"]]
    assert se_repiten(sopa1, lista, 3) == True
    assert se_repiten(sopa2, lista, 3) == True
    assert se_repiten(sopa3, lista, 3) == False

#--------------------------------------------------------------------------------------

def test_horizontal():
    sopa1 = [["s","o","q"],["s","o","l"],["p","q","l"]]
    sopa2 = [["s","o","s"],["t","e","o"],["p","q","j"]] 
    assert horizontal(0, 1, sopa1, "sol", 3) == 1
    assert horizontal(1, 0, sopa2, "os", 3) == 2

#--------------------------------------------------------------------------------------

def test_vertical():
    sopa1 = [["s","r","q"],["o","e","j"],["l","q","l"]]
    sopa2 = [["s","p","w"],["o","z","a"],["s","r","v"]] 
    assert vertical(0, 0, sopa1, "sol", 3) == 1
    assert vertical(0, 1, sopa2, "os", 3) == 2

#--------------------------------------------------------------------------------------

def test_diagonales():
    sopa1 = [["s","h","q"],["o","o","j"],["l","q","l"]]
    sopa2 = [["s","m","s"],["p","o","a"],["s","r","s"]] 
    assert diagonales(0, 0, sopa1, "sol", 3) == 1
    assert diagonales(1, 1, sopa2, "os", 3) == 4