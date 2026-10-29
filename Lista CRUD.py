#Programa CRUD de una LISTA

#Declaracion de variables inciales.

mi_lista = []
lista_menu = ["1. Agregar", "2. Lectura", "3. Modificar", "4. Eliminar", "5. Cerrar"]
#Funciones.

def separador():
    print("-"*52)

#Esto es simplemente para estetica en todo el codigo.
def menu():
    for r_menu in lista_menu:
        print(r_menu)

def l_lista():
    print("Elementos de la lista.")
    for r_lec in mi_lista:
        print(r_lec)

#Bucle principal.

while True:
    print("Bienvenido")
    menu()
    separador()
    try:
        selector = int(input("Escribe un numero dentro de tu preferencia: "))
        separador()
    except ValueError:
        print("Ingresa un numero valido.")
        input(...)
        separador()
    else:

        match selector:
            case 1:
                #Agregar elementos.
                print("Has seleccionado agregar.\n")
                while True:
                    agregar = input("Escribe algo dentro de tu preferencia: ").strip()
                    separador()
                    if agregar.lower() == "cerrar":
                        break
                    elif agregar == "":
                        print("No puede agregar elemento vacios.")
                    else:
                        mi_lista.append(agregar)
                        print("Se ha agregado correctamente.")
                    input("...")
                    separador()

            case 2:
                #Lectura de lista.
                print("Has Sseleccionado leer de lista.\n")
                if mi_lista:

                    for r_lista in mi_lista:
                        #Esto permitirá ver cada elemento y la cantidad exacta de letras de cada elemento
                        print(f'"{r_lista}" tiene: {len(r_lista)} caracter/es.')
                    l_conteo = len(mi_lista)
                    print(f"La lista contiene: {l_conteo} elemento/s.")
                    separador()
                else:
                    print("La lista no tiene elementos.")
                    input("...")
                    separador()

            case 3:
                #Modificar elementos de una lista.
                if mi_lista:
                    print("Has seleccionado modificar elementos. ")
                    while True:
                        l_lista()
                        e_actual = input("Escribe el elemento que deseas modificar: ").strip()
                        if e_actual.lower() == "cerrar":
                            break
                        elif e_actual == "":
                            print("No es un elento valido.")
                        else:
                            if e_actual in mi_lista:
                                print(f"El elemento seleccionado es: {e_actual}")
                                e_nuevo = input("Escribe el elemento nuevo: ").strip()

                                if e_nuevo.lower() == "cerrar":
                                    continue
                                elif e_nuevo == "":
                                    print("Lo que ingresas no es valido.")
                                else:
                                    if e_nuevo:
                                        posicion = mi_lista.index(e_actual)
                                        mi_lista[posicion] = e_nuevo
                                        print("Se ha actualizado el elemento.")
                            else:
                                print("El elemento no está en la lista.")
                        input("...")
                        l_lista()
                        separador()
                else:
                    print("La lista no tiene elementos.")
                    input("...")
                    separador()
            case 4:
                #Eliminar elemento de una lista

                if mi_lista:
                    print("Has seleccionado eliminar elemento.")
                    while True:
                        l_lista()
                        e_eliminar = input("Esrcibe el elemento que deseas eliminar: ").strip()

                        if e_eliminar.lower() == "cerrar":
                            break
                        elif e_eliminar == "":
                            print("No es un elemento valido.")
                        else:
                            if e_eliminar in mi_lista:
                                mi_lista.remove(e_eliminar)
                            else:
                                print("No se encuentra en la lista.")
                        input("...")
                        l_lista()
                        separador()
                else:
                    print("La lista está vacia")
                    input("...")
                    separador()
            case 5:
                #Cerrar sistema.
                print("Cerrando sistema....")
                break

            case _:
                print("Opción no válida. Selecciona un número del 1 al 5")
                input("...")
                separador()



