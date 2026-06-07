import random

aerolineas = ["AA", "LAT", "FLY", "EU", "QAT", "JET"]
destinos = ["Madrid", "Barcelona", "Buenos Aires", "Nueva York", "Miami"]
estados = ["Programado", "Embarcando", "En vuelo", "Cancelado"]
tiposVuelo = ["Nacional", "Internacional"]


def inicio():
    '''Muestra las opciones de inicio'''
    # Autor/es principal/es de la funcion: Tomas Gadaleta

    print("========================================")
    print("SISTEMA DE GESTIÓN: SKYBRIDGE AIRLINES")
    print("Ingrese:")
    print()
    print("1: Registrar vuelo (Alta)")
    print("2: Salir")
    print()
    print("========================================")


def tipoIngreso():
    '''Muestra las opciones de tipo de ingreso (Alta)'''
    # Autor/es principal/es de la funcion: Tomas Gadaleta

    print("========================================")
    print("Tipo de ingreso:")
    print("Ingrese:")
    print()
    print("1: Aleatorio")
    print("2: Por consola")
    print()
    print("========================================")


def validacionCodigo(codigo, vuelos):
    '''Verifica que el codigo ingresado sea valido'''
    # Autor/es principal/es de la funcion: Santino Nasuti

    if len(codigo) < 4 or len(codigo) > 10:
        return False
    
    if not codigo.isalnum():
        return False
    
    for vuelo in vuelos:
        if vuelo[0] == codigo:
            return False
    
    return True


def crearCodigoVuelo(aerolineas, vuelos):
    '''Genera aleatoriamente un codigo de vuelo'''
    # Autor/es principal/es de la funcion: Tomas Gadaleta y Moro Bussolini

    while True:
        aerolinea = random.choice(aerolineas)
        num = random.randint(1, 999)
        num = str(num).zfill(3)
        codigo = aerolinea + num

        if validacionCodigo(codigo, vuelos):
            # Si el codigo es valido, sale del while con un break
            break

    return codigo


def crearDestino(destinos):
    '''Genera aleatoriamente un destino de vuelo'''
    # Autor/es principal/es de la funcion: Tomas Gadaleta y Moro Bussolini

    destino = random.choice(destinos)
    return destino


def crearHorario():
    '''Genera aleatoriamente un horario de vuelo (respetando el modelo HH:MM)'''
    # Autor/es principal/es de la funcion: Tomas Gadaleta y Moro Bussolini

    hora = random.randint(0, 24)
    minutos = random.randint(0, 59)
    horario = str(hora).zfill(2) + ":" + str(minutos).zfill(2)
    return horario


def crearCantPasajeros():
    '''Genera aleatoriamente una cantidad de pasajeros de vuelo'''
    # Autor/es principal/es de la funcion: Tomas Gadaleta y Moro Bussolini

    cantPasajeros = random.randint(1, 300)
    return cantPasajeros


def crearPesoEquipajes():
    '''Genera aleatoriamente un peso de equipaje despachado de vuelo'''
    # Autor/es principal/es de la funcion: Tomas Gadaleta y Moro Bussolini

    peso = random.uniform(10000, 30000)
    peso = round(peso, 2)
    return peso


def crearEstado(estados):
    '''Genera aleatoriamente un estado operativo de vuelo'''
    # Autor/es principal/es de la funcion: Tomas Gadaleta y Moro Bussolini

    estado = random.choice(estados)
    return estado


def crearTipoVuelo(tiposVuelo):
    '''Genera aleatoriamente un tipo de vuelo'''
    # Autor/es principal/es de la funcion: Tomas Gadaleta y Moro Bussolini

    tipo = random.choice(tiposVuelo)
    return tipo


def generarVuelosAleatorios(vuelos):
    '''Genera aleatoriamente "n" vuelos. "n" se pide que sea ingresado por consola'''
    # Autor/es principal/es de la funcion: Tomas Gadaleta y Moro Bussolini

    print()
    n = int(input("Ingrese la cantidad de vuelos a generar: "))
    print()
    print("Vuelos generados aleatoriamente:")
    print()
    for i in range(n):
        codigo = crearCodigoVuelo(aerolineas, vuelos)
        print("Codigo de vuelo:", codigo)

        destino = crearDestino(destinos)
        print("Destino:", destino)
        
        horario = crearHorario()
        print("Horario de salida:", horario)
        
        cantPasajeros = crearCantPasajeros()
        print("Cantidad de pasajeros:", cantPasajeros)
        
        peso = crearPesoEquipajes()
        print("Peso de equipaje despachado:", peso, "KG")
        
        estado = crearEstado(estados)
        print("Estado de vuelo:", estado)
        
        tipo = crearTipoVuelo(tiposVuelo)
        print("Tipo de vuelo:", tipo)
        
        vuelos.append([codigo, destino, horario, cantPasajeros, peso, estado, tipo])
        print()


def mostrarOpciones():
    '''Muestra las opciones del menu principal'''
    # Autor/es principal/es de la funcion: Moro Bussolini

    print("========================================")
    print("SISTEMA DE GESTIÓN: SKYBRIDGE AIRLINES")
    print()
    print("1: Registrar vuelo (Alta)")
    print("2: Eliminar vuelo (Baja)")
    print("3: Modificar vuelo (Modficacion)")
    print("4: Informe General (Visualizacion de Datos)")
    print("5: Salir")
    print()
    print("========================================")


def ingresarOpcion(desde, hasta):
    '''Valida que se ingrese una opcion entre dos parametros (desde y hasta), ingresados por parametros'''
    # Autor/es principal/es de la funcion: Moro Bussolini

    opcion = int(input("Elija alguna opcion: "))
    while opcion < desde or opcion > hasta:
        opcion = int(input("Por favor, elija alguna opcion valida: "))
    return opcion


def ingresarCodigoManual(vuelos):
    '''Ingresa manualmente el codigo de vuelo y valida que no exista ya'''
    # Autor/es principal/es de la funcion: Santino Nasuti

    while True:
        aerolinea = input("Ingrese la aerolinea (AA, LAT, FLY, EU, QAT, JET): ").upper()
        while aerolinea not in aerolineas:
            aerolinea = input("Error. Ingrese una aerolinea valida: ").upper()

        numero = int(input("Ingrese el numero de vuelo (1-999): "))
        while numero < 1 or numero > 999:
            numero = int(input("Error. Ingrese un numero entre 1 y 999: "))
        codigo = aerolinea + str(numero).zfill(3)

        if validacionCodigo(codigo, vuelos):
            # Si el codigo es valido, sale del while con un break
            break

        print()
        print("El codigo ingresado es invalido o ya existe. Por favor, intente de nuevo.")
        print()

    return codigo



def ingresarDestinoManual():
    '''Ingresa el lugar de destino manualmente y controla que no este vacio'''
    # Autor/es principal/es de la funcion: Santino Nasuti

    lugar = input("Ingrese el lugar de destino: ").capitalize()
    while len(lugar) < 1:
        print("Error.")
        lugar = input("Ingrese el lugar de destino: ").capitalize()
    return lugar


def ingresarHorarioManual():
    '''Ingresa el horario manualmnete y valida que cumpla con el formato HH:MM'''
    # Autor/es principal/es de la funcion: Santino Nasuti
    
    hora = int(input("Ingrese la hora del horario de salida del vuelo (0-23): "))
    while hora < 0 or hora > 23:
            print("Error, no esta en el rango valido (0-23).")
            hora = int(input("Ingrese la hora del horario de salida del vuelo (0-23): "))
    
    minutos = int(input("Ingrese los minutos del horario de salida del vuelo (0-59): "))
    while minutos < 0 or minutos > 59:
            print("Error,ya no esta en el rango valido (0-59).")
            minutos = int(input("Ingrese los minutos del horario de salida del vuelo (0-59): "))

    horario = str(hora).zfill(2) + ":" + str(minutos).zfill(2)  
    return horario


def ingresarPasajerosManual():
    '''Ingresa la cantidad de pasajeros manualmente y valida que no sea negativo'''
    # Autor/es principal/es de la funcion: Santino Nasuti

    cant_pasajeros = int(input("Ingrese la cantidad de pasajeros: "))
    while cant_pasajeros < 0:
        print("No se pueden ingresar numeros negativos.")
        cant_pasajeros = int(input("Ingrese la cantidad de pasajeros: "))
    return cant_pasajeros


def ingresarPesoManual():
    '''Ingresa el peso del equipaje manualmente y controla que no sea negativo'''
    # Autor/es principal/es de la funcion: Santino Nasuti

    equipaje = float(input("Ingrese el peso del equipaje: "))
    while equipaje < 0:
        print("Error, el peso no puede ser negativo.")
        equipaje = float(input("Ingrese el peso del equipaje: "))

    peso = round(equipaje, 2)

    return peso


def mostrarEstadosOperativos():
    '''Muestra las opciones para ingresar un estado operativo'''
    # Autor/es principal/es de la funcion: Santino Nasuti

    print()
    print("Estados Operativos:")
    print("1: Programado")
    print("2: Embarcando")
    print("3: En vuelo")
    print("4: Cancelado")
    print()

def ingresarEstadoManual():
    '''Ingresa el estado operativo manualmente'''
    # Autor/es principal/es de la funcion: Santino Nasuti

    mostrarEstadosOperativos()
    opcion = ingresarOpcion(1,4)

    if opcion == 1:
        estado = "Programado"
    elif opcion == 2:
        estado = "Embarcando"
    elif opcion == 3:
        estado = "En vuelo"
    else:
        estado = "Cancelado"
    
    return estado

    

def ingresarTipoManual():
    '''Ingresa el tipo del vuelo y controla que sea Nacional o Internacional'''
    # Autor/es principal/es de la funcion: Santino Nasuti

    categoria = input("Indique el tipo del vuelo (Nacional o Internacional): ").capitalize()
    while categoria != "Nacional" and categoria != "Internacional":
        print("Error.")
        categoria = input("Indique el tipo del vuelo (Nacional o Internacional): ").capitalize()

    return categoria



def ingresoManual(vuelos):
    '''Permite ingresar N vuelos manualmente. N se pregunta por consola'''
    # Autor/es principal/es de la funcion: Santino Nasuti

    n = int(input("Ingrese cuantos vuelos desea dar de alta: "))
    while n <= 0:
        print("Por favor, ingrese una cantidad de vuelos a agregar valida.")
        n = int(input("Ingrese cuantos vuelos desea dar de alta: "))

    for i in range(n):
        codigo = ingresarCodigoManual(vuelos)
        lugar = ingresarDestinoManual()
        horario = ingresarHorarioManual()
        cant_pasajeros = ingresarPasajerosManual()
        equipaje = ingresarPesoManual()
        estado = ingresarEstadoManual()
        categoria = ingresarTipoManual()

        vuelo = [
            codigo,
            lugar,
            horario,
            cant_pasajeros,
            equipaje,
            estado,
            categoria
        ]

        vuelos.append(vuelo)

    if n == 1:
        print()
        print("El vuelo se ha agregado correctamente.")
    else:
        print()
        print("Los vuelos se han agregado correctamente.")


def mostrarOpcionesEliminacion():
    '''Muestra las opciones de elimnacion de vuelos'''
    # Autor/es principal/es de la funcion: Matias Cross

    print()
    print("========================================")
    print("Eliminacion de vuelos:")
    print("Ingrese:")
    print()
    print("1: Si desea ingresar algun codigo para eliminar un vuelo")
    print("2: Si desea volver al menu principal")
    print("========================================")
    print()


def eliminar_vuelo(vuelos):
    '''Permite eliminar un vuelo ingresando su codigo y validando que exista. Tambien Pide una segunda confirmacion'''
    # Autor/es principal/es de la funcion: Matias Cross

    mostrarOpcionesEliminacion()
    opcion = ingresarOpcion(1,2)

    while opcion == 1:
        print()
        codigo = input("Ingrese el código del vuelo a eliminar: ").upper()

        encontrado = False

        for i in range(len(vuelos)):

            if vuelos[i][0] == codigo:

                encontrado = True

                if vuelos[i][5] != "Cancelado":
                    print()
                    print("Solo se pueden eliminar vuelos cancelados.")
                    return

                confirmar = input("¿Seguro que desea eliminar el vuelo? (SI/NO): ").upper()
                while confirmar != "SI" and confirmar != "NO":
                    print("Por favor, ingrese una opcion valida.")
                    confirmar = input("¿Seguro que desea eliminar el vuelo? (SI/NO): ").upper()

                if confirmar == "SI":
                    vuelos.pop(i)
                    print()
                    print("Vuelo eliminado correctamente.")
                    print()
                    break
                else:
                    print()
                    print("Eliminación cancelada.")
                    print()
                    break

        if not encontrado:
            print("No se encontró un vuelo con ese código.")
        
        mostrarOpcionesEliminacion()
        opcion = ingresarOpcion(1,2)

    print()
    print("Se ha finalizado la eliminacion de vuelos.")

    
def mostrarOpcionesModificacion():
    '''Muestra las opciones de modificacion de vuelos'''
    # Autor/es principal/es de la funcion: Moro Bussolini
    
    print()
    print("========================================")
    print("Opciones de Modificacion de Vuelos:")
    print("Ingrese:")
    print()
    print("1: Modificar Destino de vuelo.")
    print("2: Modificar Horario de Salida de vuelo.")
    print("3: Modificar Cantidad de Pasajeros de vuelo.")
    print("4: Modificar Peso Total de Equipaje Despachado de vuelo.")
    print("5: Modificar Estado Operativo de vuelo.")
    print("6: Modificar Tipo de vuelo.")
    print("7: Terminar modificacion.")
    print()
    print("========================================")
    print()


def modificarVuelo(vuelos):
    '''Permite buscar un vuelo por su codigo y modificar uno o mas atributos'''
    # Autor/es principal/es de la funcion: Moro Bussolini

    codigo = input("Ingrese el Codigo del Vuelo del cual quiere realizar una modificacion: ")

    vuelo_a_modificar = -1

    while vuelo_a_modificar == -1:
        for i in range(len(vuelos)):
            if vuelos[i][0] == codigo:
                vuelo_a_modificar = i
                break
        
        if vuelo_a_modificar == -1:
            print("El codigo ingresado no existe. Intente de nuevo")
            codigo = input("Ingrese el Codigo del Vuelo del cual quiere realizar una modificacion: ")
    
    
    mostrarOpcionesModificacion()
    opcion = ingresarOpcion(1,7)

    while opcion != 7:
        if opcion == 1:
            destino = ingresarDestinoManual()
            vuelos[vuelo_a_modificar][1] = destino
            print("El destino del vuelo fue modificado.")
        
        elif opcion == 2:
            horario = ingresarHorarioManual()
            vuelos[vuelo_a_modificar][2] = horario
            print("El horario del vuelo fue modificado.")
        
        elif opcion == 3:
            cant_pasajeros = ingresarPasajerosManual()
            vuelos[vuelo_a_modificar][3] = cant_pasajeros
            print("La cantidad de pasajeros del vuelo fue modificado.")
        
        elif opcion == 4:
            peso = ingresarPesoManual()
            vuelos[vuelo_a_modificar][4] = peso
            print("El peso de equipaje despachado del vuelo fue modificado.")
        
        elif opcion == 5:
            estado = ingresarEstadoManual()
            vuelos[vuelo_a_modificar][5] = estado
            print("El estado operativo del vuelo fue modificado.")
        
        else:
            tipo = ingresarTipoManual()
            vuelos[vuelo_a_modificar][6] = tipo
            print("El tipo del vuelo fue modificado.")
        
        mostrarOpcionesModificacion()
        opcion = ingresarOpcion(1,7)

    print()
    print("Se han realizado las modificaciones del vuelo.")


def mostrarInformeGeneral(vuelos):
    '''Muestra un informe general de los vuelos'''
    # Autor/es principal/es de la funcion: Santiago Molina

    print()
    print("INFORME GENERAL - VUELOS REGISTRADOS")
    print()

    if len(vuelos) == 0:
        print("No hay vuelos registrados en el sistema.")
        return

    ordenados = []
    for i in range(len(vuelos)):
        ordenados.append(vuelos[i])

    # ordenar de mayor a menor cantidad de pasajeros; si empatan, destino alfabetico
    for i in range(len(ordenados)):
        for j in range(i + 1, len(ordenados)):
            pasajerosI = ordenados[i][3]
            pasajerosJ = ordenados[j][3]
            destinoI = ordenados[i][1]
            destinoJ = ordenados[j][1]

            intercambiar = False
            if pasajerosJ > pasajerosI:
                intercambiar = True
            elif pasajerosJ == pasajerosI and destinoJ < destinoI:
                intercambiar = True

            if intercambiar:
                aux = ordenados[i]
                ordenados[i] = ordenados[j]
                ordenados[j] = aux

    for vuelo in ordenados:
        print("Codigo de vuelo:", vuelo[0])
        print("Destino:", vuelo[1])
        print("Horario de salida:", vuelo[2])
        print("Cantidad de pasajeros:", vuelo[3])
        print("Peso de equipaje despachado:", vuelo[4], "KG")
        print("Estado de vuelo:", vuelo[5])
        print("Tipo de vuelo:", vuelo[6])
        print()


def main():
    '''Ejecucion principal del programa'''
    # Autor/es principal/es de la funcion: Tomas Gadaleta

    vuelos = []
    opcion = 0

    while opcion != 5:
        if len(vuelos) == 0:
            # Si no hay vuelos, solo se muestran las opciones de dar de alta y de salir

            inicio()
            opcionAlta = ingresarOpcion(1,2)

            if opcionAlta == 1:
                tipoIngreso()
                opcionAlta = ingresarOpcion(1,2)

                if opcionAlta == 1:
                    generarVuelosAleatorios(vuelos)
                else:
                    ingresoManual(vuelos)

            else:
                break

        else:
            # Si hay vuelos, se muestran todas las opciones

            mostrarOpciones()
            opcion = ingresarOpcion(1,5)

            if opcion == 1:
                tipoIngreso()
                opcionAlta = ingresarOpcion(1,2)
                
                if opcionAlta == 1:
                    generarVuelosAleatorios(vuelos)
                else:
                    ingresoManual(vuelos)

            elif opcion == 2:
                eliminar_vuelo(vuelos)

            elif opcion == 3:
                modificarVuelo(vuelos)

            elif opcion == 4:
                mostrarInformeGeneral(vuelos)

    print()
    print("Se ha finalizado la ejecucion del sistema.")
    print()

main()