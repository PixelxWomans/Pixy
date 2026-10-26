lista = []
valido = True

while valido:
    print("Selecciona dentro de tu preferencia \n1. Agregar \n2. Eliminar \n3. Salir")

    try:
        selector = int(input("Escribe un numero dentro de tu preferencia: "))
    except ValueError:
        print("No es un digito valido.")
        input("...")
    else:
        match selector:
            #Agregar elementos
            case 1:
                #bucle 
                while valido:
                    #Captura excepciones
                    try:
                        print("\n Has seleccionado agregar.\n")
                        print(f"La lista actual es: {lista}")
                        #Analisa si la lista tiene contenido para indicar los elementos agregados.
                        if lista:
                            print("Escribe 'cerrar' para ir hacia atras.\n")
                            agregar = input("Escribe algo: ")
                            
                            #Indica cierre de bucle
                            if agregar.lower() == "cerrar":
                                break

                        #En caso de que no haya elementos   
                        else:
                            
                            print("No hay elementos agregados")
                            print("Escribe 'cerrar' para ir hacia atras.\n")
                            agregar = input("Escribe algo: ")

                            if agregar.lower() == "cerrar":
                                break
                    #Captura la excepcion
                    except ValueError:
                        print("No has ingresado algo valido.")
                        print("---------------------------------------------------")
                        input("...")
                        
                        
                    #Si todo va bien, agrega el elemento a la lista
                    else:
                        lista.append(agregar)

                        print("Se ha agregado a la lista correctamente.")
                        print(f"La lista actual es: {lista}")
                        print("---------------------------------------------------")
            #Eliminar elementos
            case 2:
                while valido:
                    try:
                        print("\nHas seleccionado eliminar.\n")
                        print(f"La lista actual es: {lista}")
                        if lista:
                            
                            
                            print("Escribe 'cerrar' para ir hacia atras.\n")
                            eliminar = input("Escribe algo: ")

                        #Indica cierre de bucle
                            if eliminar.lower() == "cerrar":
                                break

                        #En caso de que no haya elementos   
                        else:
                            
                            print("No hay elementos agregados")
                            print("Escribe 'cerrar' para ir hacia atras.\n")
                            eliminar = input("Escribe algo: ")

                            if eliminar.lower() == "cerrar":
                                break
                    #Captura la excepcion
                    except ValueError:
                        print("No has ingresado algo valido.")
                        print("---------------------------------------------------")
                        input("...")
                        
                    #Si todo va bien, agrega el elemento a la lista
                    else:
                        if eliminar in lista:

                            lista.remove(eliminar)
                            print("Se ha eliminado de la lista correctamente.")
                            print(f"La lista actual es: {lista}")
                            print("---------------------------------------------------")

                        else:
                            print("No se encuentra el registro.")
                            input("...")
            case 3:
                print("Saliendo del sistema")
                valido = False
                break

                            
                        
