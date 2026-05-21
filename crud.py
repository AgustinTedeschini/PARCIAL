import validacion

def mostar_heroe(Lista:list, indice:int):
    '''brief: Muestra los datos de un heroe en especifico de la lista heroes

    lista: lista de listas con datos de cada heroe\n
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
    '''brief: Recibe y valida los datos de un nuevo heroe para agregar
    a la lista

    lista: lista de listas con datos de cada heroe\n

    retorno: no retorna nada
    '''
    nombre = input("  Ingrese nombre: ")
    while nombre == "":
        nombre = input("  ERROR: Re-Ingrese nombre: ")

    identidad = input("  Ingrece identidad secreta: ")
    while identidad == "":
        identidad = input("  ERROR: Re-Ingrece identidad secreta: ")

    compania = input("  Ingrece compania: ")
    while compania != "Marvel Comics" and compania != "DC Comics":
        compania = input("  ERROR: Re-Ingrece compania: ")

    altura = input("  Ingrece altura: ")
    while validacion.validar_casteo_int(altura) == False:
        altura = input("  ERROR: Re-Ingrece altura: ")

    peso = input("  Ingrece peso: ")
    while validacion.validar_casteo_int(peso) == False:
        peso = input("  ERROR: Re-Ingrece peso: ")

    genero = input("  Ingrece genero: ")
    while genero != "M" and genero != "F" and genero != "NB":
        genero = input("  ERROR: Re-Ingrece genero: ")

    color_ojos = input("  Ingrece color de ojos: ")
    while color_ojos == "":
        color_ojos = input("  ERROR: Re-Ingrece color de ojos: ")

    color_pelo = input("  Ingrece color de pelo: ")
    while color_pelo == "":
        color_pelo = input("  ERROR: Re-Ingrece color de pelo: ")

    fuerza = input("  Ingrece fuerza: ")
    while validacion.validar_casteo_int(fuerza) == False:
        fuerza = input("  ERROR: Re-Ingrece fuerza: ")

    inteligencia = input("  Ingrece inteligencia: ")
    while validacion.validar_casteo_int(inteligencia) == False:
        inteligencia = input("  ERROR: Re-Ingrece inteligencia: ")

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