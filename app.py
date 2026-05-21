import ordenamiento
import crud

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
        crud.mostrar_lista(lista_heroes)

    elif opcion == "3" and flag2 == False:
        crud.agregar_heroe(lista_heroes)
        ultimo_indice = int(len(lista_heroes)) -1
        print("\n","Heroe agregado correctamente","\n",
        "-----------------------","\n")
        crud.mostar_heroe(lista_heroes, ultimo_indice)

    elif opcion == "4" and flag2 == False:
        nombre = str(input("    Ingrese nombre: "))
        crud.eliminar_dato(lista_heroes,0,nombre)
        print("\n","Heroe eliminado correctamente","\n",
        "-----------------------","\n","LISTA ACTUALIZADA:","\n",
        "-----------------------")
        crud.mostrar_lista(lista_heroes)

    elif opcion == "5" and flag2 == False:
        ordenamiento.ordenar_lista_menor_mayor(lista_heroes)
        print("\n","LISTA ORDENADA:","\n",
        "-----------------------")
        crud.mostrar_lista(lista_heroes)

    elif opcion == "6" and flag2 == False:
        ordenamiento.ordenar_lista_mayor_menor(lista_heroes,3)
        print("\n","EL HEROES MAS ALTO ES:","\n",
        "-----------------------","\n")
        crud.mostar_heroe(lista_heroes,0)

    elif opcion == "7" and flag2 == False:
        ordenamiento.ordenar_lista_menor_mayor(lista_heroes)
        ordenamiento.ordenar_lista_mayor_menor(lista_heroes,8)
        print("\n","EL HEROES MAS FUERTE ES:","\n",
        "-----------------------","\n")
        crud.mostar_heroe(lista_heroes,0)

    elif opcion == "8" and flag2 == False:
        ordenamiento.ordenar_lista_menor_mayor(lista_heroes,4)
        print("\n","EL HEROES MENOS PESADO ES:","\n",
        "-----------------------","\n")
        crud.mostar_heroe(lista_heroes,0)

    elif opcion == "9":
        flag == False

    else:
        print("ERROR: Lista no importada")