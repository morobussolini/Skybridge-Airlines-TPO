import random
from validaciones import *
from colorama import Fore, Style, init


# BUSQUEDA Y ORDENAMIENTO

def buscarVueloPorCodigo(vuelos, codigo):
    '''Busqueda secuencial de un vuelo por codigo. Retorna la posicion o -1 si no existe'''
    # Autor/es principal/es: Santiago Molina
    
    for i in range(len(vuelos)):
        if vuelos[i][0] == codigo:
            return i
    return -1


def codigoDisponible(vuelos, codigo):
    '''Verifica que el codigo no exista ya en el sistema usando la busqueda secuencial'''
    # Autor/es principal/es: Santiago Molina
    
    return buscarVueloPorCodigo(vuelos, codigo) == -1


def ordenarVuelos(vuelos):
    '''Ordena los vuelos de mayor a menor pasajeros. Si empatan, destino alfabetico'''
    # Autor/es principal/es: Santiago Molina
    
    for i in range(len(vuelos)):
        for j in range(i + 1, len(vuelos)):
            pasajerosI = vuelos[i][5]
            pasajerosJ = vuelos[j][5]
            destinoI = vuelos[i][2]
            destinoJ = vuelos[j][2]

            intercambiar = False
            if pasajerosJ > pasajerosI:
                intercambiar = True
            elif pasajerosJ == pasajerosI and destinoJ < destinoI:
                intercambiar = True

            if intercambiar:
                auxiliar = vuelos[i]
                vuelos[i] = vuelos[j]
                vuelos[j] = auxiliar

# INGRESO DE DATOS

def ingresarEntero(mensaje, mensajeError):
    '''Ingresa un entero validando el formato antes de convertir'''
    # Autor/es principal/es: Moro Bussolini
    
    while True:
        texto = input(mensaje)
        if validarFormatoEntero(texto):
            return int(texto)
        mostrarError(mensajeError)


def ingresarEnteroEnRango(mensaje, mensajeError, minimo, maximo):
    '''Ingresa un entero validando formato y rango permitido'''
    # Autor/es principal/es: Moro Bussolini
    
    while True:
        texto = input(mensaje)
        if validarFormatoEntero(texto):
            numero = int(texto)
            if numero >= minimo and numero <= maximo:
                return numero
        mostrarError(mensajeError)


def ingresarDecimalPositivo(mensaje, mensajeError):
    '''Ingresa un decimal positivo validando formato y valor (directo valida el peso)'''
    # Autor/es principal/es: Moro Bussolini
    
    while True:
        texto = input(mensaje)
        if validarFormatoDecimal(texto):
            numero = float(texto)
            if validarPesoEquipaje(numero):
                return round(numero, 2)
        mostrarError(mensajeError)


def ingresarTexto(mensaje, mensajeError, validarFuncion):
    '''Ingresa un texto y lo valida con la funcion recibida por parametro'''
    # Autor/es principal/es: Moro Bussolini
    
    while True:
        texto = input(mensaje)
        if validarFuncion(texto):
            return texto
        mostrarError(mensajeError)


def ingresarOpcion(desde, hasta):
    '''Valida que se ingrese una opcion entre dos parametros (desde y hasta)'''
    # Autor/es principal/es: Matias Cross
    
    while True:
        texto = input("Elija alguna opcion: ")
        if validarFormatoEntero(texto):
            opcion = int(texto)
            if validarOpcionMenu(opcion, desde, hasta):
                return opcion
        mostrarError("Por favor, elija alguna opcion valida.")


def ingresarCodigoManual(vuelos, aerolineas):
    '''Ingresa manualmente el codigo de vuelo y valida formato y si esta disponible'''
    # Autor/es principal/es: Tomas Gadaleta
    
    while True:
        aerolinea = input("Ingrese la aerolinea (AA, LAT, FLY, EU, QAT, JET): ").upper()
        while not validarAerolinea(aerolinea, aerolineas):
            mostrarError("Error. Ingrese una aerolinea valida: ")
            aerolinea = input("Ingrese la aerolinea (AA, LAT, FLY, EU, QAT, JET): ").upper()

        numero = ingresarEnteroEnRango(
            "Ingrese el numero de vuelo (1-999): ",
            "Error. Ingrese un numero entre 1 y 999.",
            1,
            999
        )

        # El .zfill agrega a la izquierda ceros si no hay nada. La cantidad de ceros se pasa por parametro
        codigo = aerolinea + str(numero).zfill(3)

        if validarFormatoCodigo(codigo) and codigoDisponible(vuelos, codigo):
            return codigo

        mostrarError("El codigo ingresado es invalido o ya existe. Por favor, intente de nuevo.")


def ingresarAeropuertoOrigenManual(aeropuertos):
    '''Ingresa el aeropuerto de origen manualmente y controla que no este vacio'''
    # Autor/es principal/es: Santino Nasuti
    
    while True:
        aeropuerto = input("Ingrese el aeropuerto de origen (JFK, MAD, EZE, MIA, BCN): ").upper()
        
        if validarAeropuertoOrigen(aeropuerto, aeropuertos):
            return aeropuerto
            
        mostrarError("Error. Ingrese un aeropuerto válido (JFK, MAD, EZE, MIA, BCN).")


def ingresarDestinoManual():
    '''Ingresa el destino manualmente y controla que no este vacio'''
    # Autor/es principal/es: Santino Nasuti
    
    destino = ingresarTexto(
        "Ingrese el lugar de destino: ",
        "Error. El destino no puede estar vacio.",
        validarDestino
    )
    return destino.title()


def ingresarHorarioManual():
    '''Ingresa el horario manualmente y valida que cumpla con el formato HH:MM'''
    # Autor/es principal/es: Santino Nasuti
    
    hora = ingresarEnteroEnRango(
        "Ingrese la hora del horario de salida del vuelo (0-23): ",
        "Error. Ingrese una hora valida entre 0 y 23.",
        0,
        23
    )
    minutos = ingresarEnteroEnRango(
        "Ingrese los minutos del horario de salida del vuelo (0-59): ",
        "Error. Ingrese minutos validos entre 0 y 59.",
        0,
        59
    )
    return str(hora).zfill(2) + ":" + str(minutos).zfill(2)


def ingresarDuracionManual():
    '''Ingresa la duracion estimada del vuelo en horas y valida que sea positiva'''
    # Autor/es principal/es: Santino Nasuti
    
    while True:
        duracion = ingresarDecimalPositivo(
            "Ingrese la duracion estimada del vuelo en horas: ",
            "Error. Debe ingresar un numero valido y mayor a 0."
        )
        if validarDuracion(duracion):
            return duracion
        mostrarError("Error. La duracion debe ser mayor a 0.")


def ingresarPasajerosManual():
    '''Ingresa la cantidad de pasajeros manualmente y valida que no sea negativa'''
    # Autor/es principal/es: Santino Nasuti
    
    while True:
        cantPasajeros = ingresarEntero(
            "Ingrese la cantidad de pasajeros: ",
            "Error. Debe ingresar un numero entero valido."
        )
        if validarCantidadPasajeros(cantPasajeros):
            return cantPasajeros
        mostrarError("No se pueden ingresar numeros negativos.")


def ingresarPesoManual():
    '''Ingresa el peso del equipaje manualmente y controla que no sea negativo'''
    # Autor/es principal/es: Santino Nasuti
    
    return ingresarDecimalPositivo(
        "Ingrese el peso del equipaje: ",
        "Error. Debe ingresar un peso valido y no negativo."
    )


def ingresarEstadoManual(estados):
    '''Ingresa el estado operativo manualmente'''
    # Autor/es principal/es: Santino Nasuti
    
    mostrarEstadosOperativos()
    opcion = ingresarOpcion(1, 4)
    # Opcion - 1 ya que los indices empiezan desde 0
    return estados[opcion - 1]


def ingresarTipoManual():
    '''Ingresa el tipo del vuelo y controla que sea Nacional o Internacional'''
    # Autor/es principal/es: Santino Nasuti
    
    while True:
        tipo = input("Indique el tipo del vuelo (Nacional o Internacional): ").capitalize()
        if validarTipoVuelo(tipo):
            return tipo
        mostrarError("Error. Debe ingresar Nacional o Internacional.")


# GENERACION ALEATORIA


def crearCodigoVuelo(vuelos, aerolineas):
    '''Genera aleatoriamente un codigo de vuelo unico'''
    # Autor/es principal/es: Tomas Gadaleta y Moro Bussolini
    
    while True:
        aerolinea = random.choice(aerolineas)
        numero = str(random.randint(1, 999)).zfill(3)
        codigo = aerolinea + numero

        if validarFormatoCodigo(codigo) and codigoDisponible(vuelos, codigo):
            return codigo


def crearHorario():
    '''Genera aleatoriamente un horario de vuelo respetando el modelo HH:MM'''
    # Autor/es principal/es: Tomas Gadaleta y Moro Bussolini
    
    hora = random.randint(0, 23)
    minutos = random.randint(0, 59)
    return str(hora).zfill(2) + ":" + str(minutos).zfill(2)


def crearDatosVueloAleatorio(vuelos, aerolineas, destinos, estados, tiposVuelo, aeropuertos):
    '''Genera todos los datos de un vuelo de forma aleatoria'''
    # Autor/es principal/es: Tomas Gadaleta y Moro Bussolini
    
    codigo = crearCodigoVuelo(vuelos, aerolineas)
    aeropuerto = random.choice(aeropuertos)
    destino = random.choice(destinos)
    horario = crearHorario()
    duracion = round(random.uniform(1,20), 1)
    cantPasajeros = random.randint(1, 300)
    peso = round(random.uniform(1000, 30000), 2)
    estado = random.choice(estados)
    tipo = random.choice(tiposVuelo)
    return [codigo, aeropuerto, destino, horario, duracion, cantPasajeros, peso, estado, tipo]


# MENUS

def mostrarTitulo(texto):
    '''Muestra los titulos de menu de color verde'''
    # Autor/es principal/es: Moro Bussolini

    print(Fore.GREEN, texto.upper(), Style.RESET_ALL)


def mostrarError(texto):
    '''Muestra los mensajes de error de color rojo'''
    # Autor/es principal/es: Moro Bussolini

    print(Fore.RED, texto, Style.RESET_ALL)


def inicio():
    '''Muestra las opciones de inicio cuando no hay vuelos cargados'''
    # Autor/es principal/es: Tomas Gadaleta
    
    mostrarTitulo("========================================")
    mostrarTitulo("SISTEMA DE GESTION: SKYBRIDGE AIRLINES")
    print("Ingrese:")
    print()
    print("1: Registrar vuelo (Alta)")
    print("2: Administrar Catálogos (Aerolíneas/Destinos)")
    print("3: Salir")
    print()
    mostrarTitulo("========================================")


def mostrarOpciones():
    '''Muestra las opciones del menu principal'''
    # Autor/es principal/es: Tomas Gadaleta
    
    mostrarTitulo("========================================")
    mostrarTitulo("SISTEMA DE GESTION: SKYBRIDGE AIRLINES")
    print()
    print("1: Registrar vuelo (Alta)")
    print("2: Eliminar vuelo (Baja)")
    print("3: Modificar vuelo (Modificacion)")
    print("4: Informe General (Visualizacion de Datos)")
    print("5: Administrar Catálogos (Aerolíneas/Destinos)")
    print("6: Reporte de Aerolinea")
    print("7: Reporte de Destinos")
    print("8: Reporte Matricial")
    print("9: Salir")
    print()
    mostrarTitulo("========================================")


def tipoIngreso():
    '''Muestra las opciones de tipo de ingreso (Alta)'''
    # Autor/es principal/es: Tomas Gadaleta
    
    mostrarTitulo("========================================")
    mostrarTitulo("Tipo de ingreso:")
    print("Ingrese:")
    print()
    print("1: Aleatorio")
    print("2: Por consola")
    print()
    mostrarTitulo("========================================")


def mostrarEstadosOperativos():
    '''Muestra las opciones para ingresar un estado operativo'''
    # Autor/es principal/es: Santino Nasuti
    
    print()
    mostrarTitulo("Estados Operativos:")
    print("1: Programado")
    print("2: Embarcando")
    print("3: En vuelo")
    print("4: Cancelado")
    print()


def mostrarOpcionesEliminacion():
    '''Muestra las opciones de eliminacion de vuelos'''
    # Autor/es principal/es: Matias Cross
    
    mostrarTitulo("========================================")
    mostrarTitulo("Eliminacion de vuelos:")
    print("Ingrese:")
    print()
    print("1: Si desea ingresar algun codigo para eliminar un vuelo")
    print("2: Si desea volver al menu principal")
    mostrarTitulo("========================================")


def mostrarOpcionesModificacion():
    '''Muestra las opciones de modificacion de vuelos'''
    # Autor/es principal/es: Moro Bussolini
    
    mostrarTitulo("========================================")
    mostrarTitulo("Opciones de Modificacion de Vuelos:")
    print("Ingrese:")
    print()
    print("1: Modificar Aeropuerto de Origen del vuelo.")
    print("2: Modificar Destino de vuelo.")
    print("3: Modificar Horario de Salida de vuelo.")
    print("4: Modificar Duracion del vuelo.")
    print("5: Modificar Cantidad de Pasajeros de vuelo.")
    print("6: Modificar Peso Total de Equipaje Despachado de vuelo.")
    print("7: Modificar Estado Operativo de vuelo.")
    print("8: Modificar Tipo de vuelo.")
    print("9: Terminar modificacion.")
    print()
    mostrarTitulo("========================================")


def mostrarMenuCatalogos():
    '''Muestra las opciones para la administración de catálogos'''
    # Autor/es principal/es: Tomas Gadaleta

    print()
    mostrarTitulo("========================================")
    mostrarTitulo("ADMINISTRACIÓN DE CATÁLOGOS")
    print("1: Administrar Catálogo de Aerolíneas")
    print("2: Administrar Catálogo de Destinos")
    print("3: Volver al menú principal")
    print()
    mostrarTitulo("========================================")


def subMenuOpcionesCatalogos():
    '''Submenú de acciones permitidas para cada catálogo'''
    # Autor/es principal/es: Tomas Gadaleta

    print()
    print("1: Agregar nuevo elemento")
    print("2: Modificar elemento existente (por posición)")
    print("3: Quitar elemento existente (por posición)")
    print("4: Volver atrás")
    print()


def mostrarVuelo(vuelo):
    '''Muestra los datos de un vuelo en pantalla'''
    # Autor/es principal/es: Santiago Molina
    
    print("Codigo de vuelo:", vuelo[0])
    print("Aeropuerto de origen:", vuelo[1])
    print("Destino:", vuelo[2])
    print("Horario de salida:", vuelo[3])
    print("Duracion de vuelo estimada:", vuelo[4], "horas")
    print("Cantidad de pasajeros:", vuelo[5])
    print("Peso de equipaje despachado:", vuelo[6], "KG")
    print("Estado de vuelo:", vuelo[7])
    print("Tipo de vuelo:", vuelo[8])
    print()


# OPERACIONES PRINCIPALES


def ingresoManual(vuelos, aerolineas, estados, aeropuertos):
    '''Permite ingresar N vuelos manualmente. N se pregunta por consola'''
    # Autor/es principal/es: Santino Nasuti
    
    cantidad = ingresarEnteroEnRango(
        "Ingrese cuantos vuelos desea dar de alta (1-50): ",
        "Por favor, ingrese una cantidad de vuelos a agregar valida.",
        1,
        50
    )

    for i in range(cantidad):
        vuelo = [
            ingresarCodigoManual(vuelos, aerolineas),
            ingresarAeropuertoOrigenManual(aeropuertos),
            ingresarDestinoManual(),
            ingresarHorarioManual(),
            ingresarDuracionManual(),
            ingresarPasajerosManual(),
            ingresarPesoManual(),
            ingresarEstadoManual(estados),
            ingresarTipoManual()
        ]
        vuelos.append(vuelo)

    print()
    if cantidad == 1:
        print("El vuelo se ha agregado correctamente.")
    else:
        print("Los vuelos se han agregado correctamente.")


def generarVuelosAleatorios(vuelos, aerolineas, destinos, estados, tiposVuelo, aeropuertos):
    '''Genera aleatoriamente N vuelos. N se pide por consola'''
    # Autor/es principal/es: Tomas Gadaleta y Moro Bussolini
    
    print()
    cantidad = ingresarEnteroEnRango(
        "Ingrese la cantidad de vuelos a generar (1-50): ",
        "Por favor, ingrese una cantidad valida.",
        1,
        50
    )

    print()
    print("Vuelo/s generado/s aleatoriamente:")
    print()

    for i in range(cantidad):
        vuelo = crearDatosVueloAleatorio(vuelos, aerolineas, destinos, estados, tiposVuelo, aeropuertos)
        vuelos.append(vuelo)
        mostrarVuelo(vuelo)


def registrarVueloMenu(vuelos, aerolineas, destinos, estados, tiposVuelo, aeropuertos):
    '''Coordina el alta de vuelos (manual o aleatoria)'''
    # Autor/es principal/es: Tomas Gadaleta
    
    tipoIngreso()
    opcionAlta = ingresarOpcion(1, 2)

    if opcionAlta == 1:
        generarVuelosAleatorios(vuelos, aerolineas, destinos, estados, tiposVuelo, aeropuertos)
    else:
        ingresoManual(vuelos, aerolineas, estados, aeropuertos)


def eliminarVuelo(vuelos):
    '''Permite eliminar un vuelo cancelado ingresando su codigo. Pide una segunda confirmacion'''
    # Autor/es principal/es: Matias Cross
    
    mostrarOpcionesEliminacion()
    opcion = ingresarOpcion(1, 2)

    while opcion == 1:
        print()
        codigo = input("Ingrese el codigo del vuelo a eliminar: ").upper()
        posicion = buscarVueloPorCodigo(vuelos, codigo)

        if posicion == -1:
            print("No se encontro un vuelo con ese codigo.")
        elif vuelos[posicion][7] != "Cancelado":
            print()
            print("Solo se pueden eliminar vuelos cancelados.")
        else:
            confirmar = input("Seguro que desea eliminar el vuelo? (SI/NO): ").upper()
            while confirmar != "SI" and confirmar != "NO":
                mostrarError("Por favor, ingrese una opcion valida.")
                confirmar = input("Seguro que desea eliminar el vuelo? (SI/NO): ").upper()

            print()
            if confirmar == "SI":
                vuelos.pop(posicion)
                print("Vuelo eliminado correctamente.")
            else:
                print("Eliminacion cancelada.")
            print()

        mostrarOpcionesEliminacion()
        opcion = ingresarOpcion(1, 2)

    print()
    print("Se ha finalizado la eliminacion de vuelos.")


def modificarVuelo(vuelos, estados, aeropuertos):
    '''Permite buscar un vuelo por codigo y modificar uno o mas atributos'''
    # Autor/es principal/es: Moro Bussolini
    
    codigo = input("Ingrese el Codigo del vuelo del cual quiere realizar una modificacion: ").upper()
    posicion = buscarVueloPorCodigo(vuelos, codigo)

    while posicion == -1:
        mostrarError("El codigo ingresado no existe. Intente de nuevo.")
        codigo = input("Ingrese el Codigo del vuelo del cual quiere realizar una modificacion: ").upper()
        posicion = buscarVueloPorCodigo(vuelos, codigo)

    mostrarOpcionesModificacion()
    opcion = ingresarOpcion(1, 9)

    while opcion != 9:
        if opcion == 1:
            vuelos[posicion][1] = ingresarAeropuertoOrigenManual(aeropuertos)
            print("El aeropuerto de origen del vuelo fue modificado.")
        elif opcion == 2:
            vuelos[posicion][2] = ingresarDestinoManual()
            print("El destino del vuelo fue modificado.")
        elif opcion == 3:
            vuelos[posicion][3] = ingresarHorarioManual()
            print("El horario del vuelo fue modificado.")
        elif opcion == 4:
            vuelos[posicion][4] = ingresarDuracionManual()
            print("La duracion del vuelo fue modificada.")
        elif opcion == 5:
            vuelos[posicion][5] = ingresarPasajerosManual()
            print("La cantidad de pasajeros del vuelo fue modificada.")
        elif opcion == 6:
            vuelos[posicion][6] = ingresarPesoManual()
            print("El peso de equipaje despachado del vuelo fue modificado.")
        elif opcion == 7:
            vuelos[posicion][7] = ingresarEstadoManual(estados)
            print("El estado operativo del vuelo fue modificado.")
        else:
            vuelos[posicion][8] = ingresarTipoManual()
            print("El tipo del vuelo fue modificado.")

        mostrarOpcionesModificacion()
        opcion = ingresarOpcion(1, 9)

    print()
    print("Se han realizado las modificaciones del vuelo.")


def mostrarInformeGeneral(vuelos):
    '''Muestra un informe general de los vuelos ordenados'''
    # Autor/es principal/es: Santiago Molina
    
    print()
    print("INFORME GENERAL - VUELOS REGISTRADOS")
    print()

    ordenarVuelos(vuelos)

    for i in range(len(vuelos)):
        mostrarVuelo(vuelos[i])


# REPORTES FASE 2

def acumularDatosReportes(vuelos, indiceColumna, valorBuscado):
    '''Acumula la cantidad de vuelos, pasajeros y peso dependiendo del filtro que le pasemos'''
    # Autor/es principal/es: Santiago Molina
    cant_vuelos = 0
    total_pasajeros = 0
    total_peso = 0

    for i in range(len(vuelos)):
        coincidencia = False
        
        if indiceColumna == 0 and vuelos[i][0].startswith(valorBuscado):
            coincidencia = True
        elif indiceColumna == 2 and vuelos[i][2] == valorBuscado:
            coincidencia = True
        
        if coincidencia:
            cant_vuelos += 1
            total_pasajeros += vuelos[i][5]
            total_peso += vuelos[i][6]

    return cant_vuelos, total_pasajeros, total_peso


def existeEnLista(texto, lista):
    '''Busqueda secuencial para ver si un elemento esta en la lista'''
    # Autor/es principal/es: Santiago Molina

    for i in range(len(lista)):
        if lista[i] == texto:
            return True
    return False


def mostrarReporteAerolinea(vuelos, aerolineas):
    '''Muestra los totales de una aerolinea que elige el usuario'''
    # Autor/es principal/es: Santiago Molina

    mostrarTitulo("--- REPORTE DE AEROLINEA ---")
    
    aerolinea = input("Ingrese la aerolinea a consultar (Ej: AA, LAT, FLY): ").upper()
    
    while not existeEnLista(aerolinea, aerolineas):
        mostrarError("Error. La aerolinea no existe en el catalogo.")
        aerolinea = input("Ingrese la aerolinea a consultar: ").upper()
        
    vuelos_cant, pasajeros, peso = acumularDatosReportes(vuelos, 0, aerolinea)
    
    print()
    print("Resultados para:", aerolinea)
    print(" - Cantidad de vuelos:", vuelos_cant)
    print(" - Cantidad total de pasajeros:", pasajeros)
    print(" - Peso total de equipaje despachado:", round(peso, 2), "KG")
    print()


def ordenarListaAlfabetico(lista):
    '''Ordena una lista alfabeticamente usando burbujeo'''
    # Autor/es principal/es: Santiago Molina

    lista_ordenada = lista.copy() 
    for i in range(len(lista_ordenada)):
        for j in range(i + 1, len(lista_ordenada)):
            if lista_ordenada[j] < lista_ordenada[i]:
                aux = lista_ordenada[i]
                lista_ordenada[i] = lista_ordenada[j]
                lista_ordenada[j] = aux
    return lista_ordenada


def mostrarReporteDestinos(vuelos, destinos):
    '''Muestra los acumulados agrupados por destino y ordenados alfabeticamente'''
    # Autor/es principal/es: Santiago Molina

    mostrarTitulo("--- REPORTE DE DESTINOS ---")
    print()
    
    destinos_ordenados = ordenarListaAlfabetico(destinos)
    
    for i in range(len(destinos_ordenados)):
        destino_actual = destinos_ordenados[i]
        
        vuelos_cant, pasajeros, peso = acumularDatosReportes(vuelos, 2, destino_actual)
        
        print("Destino:", destino_actual)
        print(" - Cantidad de vuelos programados:", vuelos_cant)
        print(" - Cantidad total de pasajeros:", pasajeros)
        print(" - Peso total de equipaje:", round(peso, 2), "KG")
        print("-" * 40)


def administrarCatalogos(aerolineas, destinos):
    '''Permite modificar las listas de catálogos de aerolineas y destinos'''
    # Autor/es principal/es: Tomas Gadaleta

    mostrarMenuCatalogos()
    opcion = ingresarOpcion(1, 3)
    
    while opcion != 3:
        if opcion == 1:
            print(f"\nAerolíneas actuales: {aerolineas}")
            subMenuOpcionesCatalogos()
            opcion_sub_menu = ingresarOpcion(1, 4)
            
            if opcion_sub_menu == 1:
                nueva = input("Ingrese la sigla de la nueva aerolínea: ").upper()
                if len(nueva.strip()) >= 2 and not existeEnLista(nueva, aerolineas):
                    aerolineas.append(nueva)
                    print(f"Aerolínea '{nueva}' agregada con éxito.")
                else:
                    mostrarError("Error. Sigla inválida o ya existente.")
            elif opcion_sub_menu == 2:
                print("\nSeleccione el número de la aerolínea que desea cambiar:")
                for i in range(len(aerolineas)):
                    print(f"{i + 1}: {aerolineas[i]}")
                posicion_elegida = ingresarOpcion(1, len(aerolineas)) - 1
                
                reemplazo = input(f"Ingrese la nueva sigla para reemplazar a '{aerolineas[posicion_elegida]}': ").upper()
                if len(reemplazo.strip()) >= 2 and not existeEnLista(reemplazo, aerolineas):
                    aerolineas[posicion_elegida] = reemplazo
                    print("Catálogo modificado correctamente.")
                else:
                    mostrarError("Error. Sigla inválida o ya existente.")
            elif opcion_sub_menu == 3:
                print("\nSeleccione el número de la aerolínea que desea quitar:")
                for i in range(len(aerolineas)):
                    print(f"{i + 1}: {aerolineas[i]}")
                posicion_elegida = ingresarOpcion(1, len(aerolineas)) - 1
                
                aerolineas.pop(posicion_elegida)
                print("Elemento quitado con éxito.")

        elif opcion == 2:
            print(f"\nDestinos actuales: {destinos}")
            subMenuOpcionesCatalogos()
            opcion_sub_menu = ingresarOpcion(1, 4)
            
            if opcion_sub_menu == 1:
                nuevo = input("Ingrese el nombre del nuevo destino: ").title()
                if len(nuevo.strip()) > 0 and not existeEnLista(nuevo, destinos):
                    destinos.append(nuevo)
                    print(f"Destino '{nuevo}' agregado con éxito.")
                else:
                    mostrarError("Error. Destino inválido o ya existente.")
            elif opcion_sub_menu == 2:
                print("\nSeleccione el número del destino que desea cambiar:")
                for i in range(len(destinos)):
                    print(f"{i + 1}: {destinos[i]}")
                posicion_elegida = ingresarOpcion(1, len(destinos)) - 1
                
                reemplazo = input(f"Ingrese el nuevo nombre para reemplazar a '{destinos[posicion_elegida]}': ").title()
                if len(reemplazo.strip()) > 0 and not existeEnLista(reemplazo, destinos):
                    destinos[posicion_elegida] = reemplazo
                    print("Catálogo modificado correctamente.")
                else:
                    mostrarError("Error. Destino inválido o ya existente.")
            elif opcion_sub_menu == 3:
                print("\nSeleccione el número del destino que desea quitar:")
                for i in range(len(destinos)):
                    print(f"{i + 1}: {destinos[i]}")
                posicion_elegida = ingresarOpcion(1, len(destinos)) - 1
                
                destinos.pop(posicion_elegida)
                print("Elemento quitado con éxito.")
        
        mostrarMenuCatalogos()
        opcion = ingresarOpcion(1, 3)


def reporteMatricial(vuelos, aerolineas, estados):
    '''Genera una matriz que muestra la distribución de vuelos según aerolínea y estado operativo'''
    # Autor/es principal/es: Matias Cross

    matriz = []
    for i in range(len(aerolineas)):
        fila = []
        for j in range(len(estados)):
            fila.append(0)
        matriz.append(fila)

    for i in range(len(vuelos)):
        codigo = vuelos[i][0]
        for fila in range(len(aerolineas)):
            if codigo[0:len(aerolineas[fila])] == aerolineas[fila]:
                for columna in range(len(estados)):
                    if vuelos[i][7] == estados[columna]:
                        matriz[fila][columna] += 1

    print()
    mostrarTitulo("--- REPORTE MATRICIAL DE VUELOS ---")
    print()

    print("AEROLINEA", end=" ")
    for j in range(len(estados)):
        print(estados[j], end=" ")

    print("TOTAL")
    for i in range(len(aerolineas)):
        totalFila = 0

        print(aerolineas[i], end="\t\t")

        for j in range(len(estados)):
            print(matriz[i][j], end="\t")
            totalFila += matriz[i][j]

        print(totalFila)

    print("TOTAL", end="\t\t")

    for j in range(len(estados)):
        totalColumna = 0
        for i in range(len(aerolineas)):
            totalColumna += matriz[i][j]

        print(totalColumna, end="\t")

    print()


# PROGRAMA PRINCIPAL (main)

def main():
    '''Ejecucion principal del programa. Coordina llamadas a funciones'''
    # Autor/es principal/es: Tomas Gadaleta

    init()
    
    aerolineas = ["AA", "LAT", "FLY", "EU", "QAT", "JET"]
    destinos = ["Madrid", "Barcelona", "Buenos Aires", "Nueva York", "Miami"]
    estados = ["Programado", "Embarcando", "En vuelo", "Cancelado"]
    tiposVuelo = ["Nacional", "Internacional"]
    aeropuertos = ["JFK", "MAD", "EZE", "MIA", "BCN"]

    vuelos = []
    opcion = 0

    while opcion != 9:
        if len(vuelos) == 0:
            inicio()
            opcionAlta = ingresarOpcion(1, 3)

            if opcionAlta == 1:
                registrarVueloMenu(vuelos, aerolineas, destinos, estados, tiposVuelo, aeropuertos)
            elif opcionAlta == 2:
                administrarCatalogos(aerolineas, destinos)
            else:
                opcion = 9
        else:
            mostrarOpciones()
            opcion = ingresarOpcion(1, 9)

            if opcion == 1:
                registrarVueloMenu(vuelos, aerolineas, destinos, estados, tiposVuelo, aeropuertos)
            elif opcion == 2:
                eliminarVuelo(vuelos)
            elif opcion == 3:
                modificarVuelo(vuelos, estados, aeropuertos)
            elif opcion == 4:
                mostrarInformeGeneral(vuelos)
            elif opcion == 5:
                administrarCatalogos(aerolineas, destinos)
            elif opcion == 6:
                mostrarReporteAerolinea(vuelos, aerolineas)
            elif opcion == 7:
                mostrarReporteDestinos(vuelos, destinos)
            elif opcion == 8:
                reporteMatricial(vuelos, aerolineas, estados)

    print()
    print("Se ha finalizado la ejecucion del sistema.")
    print()

main()