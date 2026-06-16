def crear_tabla(matriz: None):

    cantidad_columnas = int(input("Ingrese la cantidad de columnas que tendrá la tabla: "))

    nombres_columnas = [0] * cantidad_columnas
    for j in range(cantidad_columnas):
        nombres_columnas[j] = input(f"Ingrese el nombre de la columna {j+1}: ")

    matriz = [nombres_columnas]

    continuar = "si"
    while continuar == "si":
        nueva_fila = [0] * cantidad_columnas
        print(f"Cargando la fila {len(matriz)}:")

        for j in range(cantidad_columnas):
            nueva_fila[j] = input(f"Ingrese dato para '{matriz[0][j]}': ")

        matriz += [nueva_fila] 

        continuar = input("¿Desea cargar otra fila? si/no: ")

    return matriz



def modificar_tabla(matriz):

    cantidad_columnas = len(matriz[0])

    cantidad_filas = len(matriz)

    print(f"Filas cargadas: Hay {cantidad_filas - 1} filas de datos (índices del 1 al {cantidad_filas - 1}).")
    fila_a_cambiar = int(input("Ingrese el número de fila a modificar: "))

    if 1 <= fila_a_cambiar < cantidad_filas:
        for j in range(cantidad_columnas):
            nuevo_valor = input(f"'{matriz[0][j]}' (actual: '{matriz[fila_a_cambiar][j]}'): ")
            matriz[fila_a_cambiar][j] = nuevo_valor
        print("se completo la modificacion")
    else:
        print("numero de fila invalido")

    return matriz



def mostrar_tabla(matriz):
    if len(matriz) == 0:
        print("la tabla esta vacia")
        return

    cantidad_columnas = len(matriz[0])
    cantidad_filas = len(matriz)

    visualizar_columnas= input("¿Desea ver todas las columnas? si/no : ")

    columnas_activas = [False] * cantidad_columnas

    if  visualizar_columnas == "si":
        for j in range(cantidad_columnas):
            columnas_activas[j] = True
    else:
        print("Seleccione las columnas que quiere ver:")
        for j in range(cantidad_columnas):
            respuesta = input(f"¿Mostrar columna '{matriz[0][j]}'? si/no: ")
            if respuesta == "si":
                columnas_activas[j] = True

        for i in range( cantidad_filas):
            for j in range( cantidad_columnas):
                if columnas_activas[j]:
                    print(matriz[i][j], end="\t")
            print("")
