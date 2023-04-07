
////////////////////////////////////////////// PROTOTIPOS DE FUNCIONES PARTE C ///////////////////////////////////////////////////////////


//cargar_palabras: FILE int** int -> int
//               : La funcion recibe el archivo a escanear, un triple-puntero y el largo maximo de las palabras.
//               : La funcion va guardando los punteros de las palabras mediante un ciclo while 
//               : que los va creando y guardando en un arreglo creciente. Esto se hace mediante dos punteros-dobles que, alternativamente, se van complementando.
//               : Cuando uno se llena, el otro se libera para luego aumentar su espacio en memoria y asi guardar mas punteros.
//               : Este proceso se repite y termina cuando se llega al final de la lista ahorrandonos la necesidad de ponerle un tope
//               : de memoria al arreglo. Finalmente con el triple-puntero le damos el valor de la direccion final del arreglo creciente al doble-puntero que este apunta,
//               : el cual se creo en la funcion main. Ademas, la funcion retorna el contador de palabras para luego usarlo en otra funcion.
int cargar_palabras(FILE* archivo, int largoMaximo, char*** triplePuntero);

//-------------------------------------------------

//ingresar_complejidad: None -> int
//                    : La funcion le pide al usuario que ingrese un numero, este puede ser 1, 2 o 3. Si el usuario
//                    : ingresa cualquier otro, se le pide que vuelva a ingresar.
int ingresar_complejidad();

//-------------------------------------------------

//escribir_archivo: FILE int** int int int int -> None
//                : La funcion recibe un archivo a escribir con sus respectivos datos. Ademas recibe el doble puntero 
//                : donde se encuentran las direcciones de las palabras. La funcion mediante un for va escribiendo en el archivo
//                : palabras aleatorias que hay almacenadas en el espacio reservado del doble puntero, asi hasta completar la 
//                : cantidad de palabras maxima ingresada por el usuario. Junto a esto escribe tambien los otros datos dados
//                : como parametros.
void escribir_archivo(FILE* archivo, char** direccionLista,int tamanioSopa,int cantidadPalabras,int complejidad,int palabrasTotales);

//-------------------------------------------------

//numero_aleatorio: int int int -> int
//                : La funcion recibe un numero entero maximo N, un arreglo de numeros y la cantidad de palabras. Devuelve un numero aleatorio 
//                : entre 0 y N fijandose que este numero no pertenezca al arreglo.
int numero_aleatorio(int numMax, int arreglo[], int cantPalabras);

//-------------------------------------------------

//esta_en_arreglo: int int int -> int
//               : La funcion toma un numero y un arreglo y se fija si este numero esta en el arreglo. 
int esta_en_arreglo(int numero, int arreglo[], int cantPalabras);