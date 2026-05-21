def mostar_heroe(Lista:list, indice:int):
    '''brief: Muestra los datos de un heroe en especifico de la lista heroes

    lista: lista de listas con datos de los heroes\n
    indice: indice del heroe a mostrar

    retorno: no retorna nada
    '''
    print("\n"," Nombre:", Lista[indice][0], "\n",
    " Identidad:",Lista[indice][1], "\n",
    " Compania:", Lista[indice][2], "\n",
    " Altura:", Lista[indice][3],"cm", "\n",
    " Peso:", Lista[indice][4],"Kg", "\n",
    " Género:", Lista[indice][5], "\n",
    " Color de ojos:", Lista[indice][6], "\n",
    " Color de pelo:", Lista[indice][7], "\n",
    " Fuerza:", Lista[indice][8], "\n",
    " Inteligencia:", Lista[indice][9], "\n")

def mostrar_lista(lista:list, indice:int = -3, dato:str = ""):
    '''brief: Muestra una lista de listas, con la posibilidad de filtrar por
    un dato en especifico

    lista: lista de listas a mostrar\n
    indice: indice la lista a comparar con el dato, utilizado para filtrar\n
    dato: dato a comparar con el indice

    retorno: no retorna nada
    '''
    for i in range(len(lista)):
        if indice == -3 or lista[i][indice] == dato:
            mostar_heroe(lista,i)

def agregar_heroe(lista:list):
    '''brief: Agrega un nuevo heroe a la lista

    lista: lista de listas con datos de los heroes\n

    retorno: no retorna nada
    '''
    nombre = input("  Ingrese nombre: ")
    identidad = (input("  Ingrece identidad secreta: "))
    compania = (input("  Ingrece compania: "))
    altura = int(input("  Ingrece altura: "))
    peso = int(input("  Ingrece peso: "))
    genero = input("  Ingrece genero: ")
    color_ojos = input("  Ingrece color de ojos: ")
    color_pelo = input("  Ingrece color de pelo: ")
    fuerza = int(input("  Ingrece fuerza: "))
    inteligencia = int(input("  Ingrece inteligencia: "))

    nuevo_dato = [nombre, identidad, compania, altura, peso, genero,
    color_ojos, color_pelo, fuerza, inteligencia]
    lista.append(nuevo_dato)

def eliminar_dato(lista:list, indice:int, dato:str):
    '''brief: Elimina un dato de la lista

    lista: lista de listas\n
    indice: indice de la lista a comparar con el dato\n
    dato: dato a comparar con el indice

    retorno: no retorna nada
    '''
    for i in range(len(lista)):
        if lista[i][indice] == dato:
            mostar_heroe(lista, i)
            lista.pop(i)
            break