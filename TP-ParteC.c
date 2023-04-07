//TP FINAL - PARTE C - Sebastian Giulianelli - legajo:(G-5739/8)

#include <stdio.h>
#include <stdlib.h> 
#include <time.h>
#include <string.h>
#include "TP-PrototiposC.h"
#include "TP-TestsC.c"



//main: None -> int
//    : La funcion principal se encarga de pedirle al usuario los datos necesarios para la sopa de letras. Luego, guarda las palabras con un doble-puntero
//    : para despues reescribir todo en un archivo de salida .txt.
int main(){

//    test_esta_en_arreglo();
//    test_ingresar_complejidad();

    srand(time(NULL));
    int tamanioSopa, cantidadPalabras, complejidad;
    char ruta[50], archivonuevo[50];
    printf("\nIngrese el nombre del archivo lemario: ");
    scanf("%s", ruta);

    printf("\nIngrese tamanio de la sopa de letras: ");
    scanf(" %d", &tamanioSopa);

    printf("\nIngrese la cantidad de palabras deseada en la sopa de letras: ");
    scanf(" %d", &cantidadPalabras);

    printf("\nIngrese la complejidad de la sopa de letras <0/1/2/3>: ");
    complejidad = ingresar_complejidad();

    printf("\nIngrese el nombre del archivo a crear: ");
    scanf("%s", archivonuevo);

    FILE* archivo;
    archivo = fopen(ruta, "r");
    int largoMaximo = 25, palabrasTotales = 0;
    char **direccionLista;
    printf("\nCargando...");
    palabrasTotales = cargar_palabras(archivo, largoMaximo, &direccionLista);
    fclose(archivo);

    FILE* archivo2;
    archivo2 = fopen(archivonuevo, "w");
    escribir_archivo(archivo2, direccionLista, tamanioSopa, cantidadPalabras, complejidad, palabrasTotales);
    fclose(archivo2);

    printf("\nArchivo creado correctamente -> %s\n", archivonuevo);
    return 0;  
}

//-------------------------------------------------

int cargar_palabras(FILE* archivo, int largoMaximo, char*** triplePuntero){
  
    int contador = 0, largoPalabra;
    char **punteroInicial, **punteroAux, *direccion,  palabra[largoMaximo];
    punteroInicial = malloc(sizeof(char *));
    while(feof(archivo) == 0){
      fgets(palabra, largoMaximo, archivo);
      direccion = malloc((strlen(palabra)+1) * sizeof(char));
      strcpy(direccion, palabra);
      
      if(contador == 0){
        punteroInicial[contador] = direccion;
      }
      else if (contador % 2 != 0){ //numero impar      
        punteroAux = malloc((contador + 1) * sizeof(char *));
        punteroAux[contador] = direccion;
        for(int i = 0; i < contador; i++){
          punteroAux[i] = punteroInicial[i];}
        free(punteroInicial);
      }
      else{ //numero par
        punteroInicial = malloc((contador + 1) * sizeof(char *));
        punteroInicial[contador] = direccion;
        for(int i = 0; i < contador; i++){
          punteroInicial[i] = punteroAux[i];}
        free(punteroAux);
      }
      contador++;
    }

    if(contador % 2 != 0)
      triplePuntero[0] = punteroInicial;
    else
      triplePuntero[0] = punteroAux;
      

    return contador;
}

//-------------------------------------------------

int ingresar_complejidad(){
 
  int complejidad;
  scanf("%d", &complejidad);
  if(complejidad >= 0 && complejidad <= 3)
    return complejidad;
  else{
    while(!(complejidad >= 0 && complejidad <= 3)){
      printf("Error, elija correctamente entre 0, 1, 2 o 3: ");
      scanf("%d", &complejidad);
    }
  }
  return complejidad;
}

//-------------------------------------------------

void escribir_archivo(FILE* archivo, char** direccionLista,int tamanioSopa,int cantidadPalabras,int complejidad,int palabrasTotales){
 
  fprintf(archivo, "DIMENSION: \n%d\n\nPALABRAS(%d):\n", tamanioSopa, cantidadPalabras);
  int indicesUsados[cantidadPalabras], numeroAleatorio;
  for(int i = 0; i < cantidadPalabras; i++)//Como al principio los indices usados no existen, se los reemplaza por -1 para permitir cualquier numero aleatorio
    indicesUsados[i] = -1;
  for(int i = 0; i<cantidadPalabras; i++){
    numeroAleatorio = numero_aleatorio(palabrasTotales, indicesUsados, cantidadPalabras);
    indicesUsados[i] = numeroAleatorio;
    if(numeroAleatorio == palabrasTotales-1)
      fprintf(archivo,"%s\n", direccionLista[numeroAleatorio]);
    else
      fprintf(archivo,"%s", direccionLista[numeroAleatorio]);
  }
  fprintf(archivo, "\nCOMPLEJIDAD: \n%d\n", complejidad);
}

//-------------------------------------------------

int numero_aleatorio(int numMax, int arreglo[], int cantPalabras){
  int numeroAleatorio = rand()%(numMax);
  while(esta_en_arreglo(numeroAleatorio, arreglo, cantPalabras))
      numeroAleatorio = rand()%numMax;
  return numeroAleatorio;
}

//-------------------------------------------------

int esta_en_arreglo(int numero, int arreglo[], int cantPalabras){
  for(int i = 0; i < cantPalabras; i++){
    if (numero == arreglo[i])
      return 1;
  }
  return 0;
}