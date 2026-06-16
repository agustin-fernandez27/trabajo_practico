def validar_rangos(num:int,minimo:int,maximo:int) -> bool:
    
    if num >= minimo and num <= maximo:
        print("cumple la condicion")
        return True
    else:
        print("no cumple la condicion")
        return False



def determinar_paridad(num : int) -> bool:

    if num % 2 == 0:
        print("es par")
        return True
    else:
        print("no es par")
        return False



def determinar_primo(numero) ->bool:
#solo divisible por el y por 1:
    divisores = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1

    if divisores == 2:
        return True

    else:
        return False



def determinar_multiplo(num:int,num2:int) -> bool:

    if num2 % num == 0:
        print("es multiplo")
        return True
    else:
        print("no es multiplo")
        return False


def determinar_recursividad (num:int):

    if num == 1:
        return 1
    else:
        return determinar_recursividad(num - 1)



def validar_ingreso(usuario : list,contraseña : list,ingreso_usuario : str,ingreso_contraseña : int) ->bool:
    while usuario != ingreso_usuario or contraseña != ingreso_contraseña:
        print("usuario o contraseña incorrecto")
        registro = input("quiere registrarse (si/no) : ")

        nuevos_usuarios = []
        nuevas_contraseñas = []

        if registro == "si":
            nuevo_ingreso = input("ingrese nombre de usuario : ")
            nueva_contraseña = int(input("ingrese contraseña : "))
            usuario = nuevo_ingreso
            contraseña = nueva_contraseña
            print("ingresando...")
            return True
        elif registro == "no":
            return False
        else:
            print("Ingrese si/no a la respuesta")

    return True