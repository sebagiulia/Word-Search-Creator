#include "TP-PrototiposC.h"
#include <stdio.h>
#include <assert.h>

///////////////////////////////////////////// TESTS FUNCIONES PARTE C /////////////////////////////////////////////////////////////

// test_esta_en_arreglo: void -> void
//                     : La funcion testea la funcion esta_en_arreglo().
void test_esta_en_arreglo(){  
    int arreglo1[] = {1,2,3,4}, arreglo2[] = {-1,-1,-1,-1};
    assert(esta_en_arreglo(3, arreglo1, 4) == 1);
    assert(esta_en_arreglo(0, arreglo1, 4) == 0);
    assert(esta_en_arreglo(1, arreglo2, 4) == 0);
    assert(esta_en_arreglo(-1, arreglo2, 4) == 1);
}

//---------------------------------------

// test_ingresar_complejidad: void -> void
//                     : La funcion testea la funcion ingresar_complejidad().
void test_ingresar_complejidad(){
    printf("Test funcion ingresar_complejidad\n");
    printf("Ingresar 0:\n");
    assert(ingresar_complejidad() == 0);
    printf("Ingresar 1:\n");
    assert(ingresar_complejidad() == 1);
    printf("Ingresar 2:\n");
    assert(ingresar_complejidad() == 2);
    printf("Ingresar 3:\n");
    assert(ingresar_complejidad() == 3);
    printf("Ingresar numero distinto de [0/1/2/3], luego ingresar 0 para terminar el test.\n");
    assert(ingresar_complejidad() == 0);
}