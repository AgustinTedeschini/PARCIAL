def mostar_heroe(Lista:list, indice:int):
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
    for i in range(len(lista)):
        if indice == -3 or lista[i][indice] == dato:
            mostar_heroe(lista,i)

def agregar_heroe(lista:list):
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
    for i in range(len(lista)):
        if lista[i][indice] == dato:
            mostar_heroe(lista, i)
            lista.pop(i)
            break

def ordenar_lista_menor_mayor(lista:list, indice:int = 0):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i][indice] > lista[j][indice]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def ordenar_lista_mayor_menor(lista:list, indice:int = 0):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i][indice] < lista[j][indice]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

flag = True
flag2 = True

while flag == True: 
    print(
        '''
        \n
        1- Importar la lista de heroes
        2- Listar todos los héroes
        3- Agregar héroe a la lista 
        4- Eliminar producto por nombre
        5- Ordenar la lista de héroes por nombre
        6- Ver héroe más alto
        7- Ver héroe más fuerte
        8- Ver héroe menos pesado
        9- Salir
        \n
        ''' )
    
    opcion = input("ingrese una opcion del menu: ")


    if opcion == "1":
        from heroes import lista_heroes
        flag2 = False
        print("\n","LISTA IMPORTADA EXITOSAMENTE")

    elif opcion == "2" and flag2 == False:
        mostrar_lista(lista_heroes)

    elif opcion == "3" and flag2 == False:
        agregar_heroe(lista_heroes)
        ultimo_indice = int(len(lista_heroes)) -1
        print("\n","Heroe agregado correctamente","\n",
        "-----------------------","\n")
        mostar_heroe(lista_heroes, ultimo_indice)

    elif opcion == "4" and flag2 == False:
        nombre = str(input("    Ingrese nombre: "))
        eliminar_dato(lista_heroes,0,nombre)
        print("\n","Heroe eliminado correctamente","\n",
        "-----------------------","\n","LISTA ACTUALIZADA:","\n",
        "-----------------------")
        mostrar_lista(lista_heroes)

    elif opcion == "5" and flag2 == False:
        ordenar_lista_menor_mayor(lista_heroes)
        print("\n","LISTA ORDENADA:","\n",
        "-----------------------")
        mostrar_lista(lista_heroes)

    elif opcion == "6" and flag2 == False:
        ordenar_lista_mayor_menor(lista_heroes,3)
        print("\n","EL HEROES MAS ALTO ES:","\n",
        "-----------------------","\n")
        mostar_heroe(lista_heroes,0)

    elif opcion == "7" and flag2 == False:
        #3 HEROES EMPATAN POR MAS FUERTE ASI QUE ORDENO ALFABETICAMENTE PRIMERO

        ordenar_lista_menor_mayor(lista_heroes)
        ordenar_lista_mayor_menor(lista_heroes,8)
        print("\n","EL HEROES MAS FUERTE ES:","\n",
        "-----------------------","\n")
        mostar_heroe(lista_heroes,0)

    elif opcion == "8" and flag2 == False:
        ordenar_lista_menor_mayor(lista_heroes,4)
        print("\n","EL HEROES MENOS PESADO ES:","\n",
        "-----------------------","\n")
        mostar_heroe(lista_heroes,0)

    elif opcion == "9":
        flag == False

    elif flag2 == True:
        print("ERROR: Lista no importada")