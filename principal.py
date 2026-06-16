from paquete.validaciones import *
from paquete.tablas import *

usuario = "juan"
contraseña = 123

ingreso_usuario = input("Ingrese nombre de usuario : ")
ingreso_contraseña = int(input("Ingrese la contraseña : "))

entro = False

acceso = validar_ingreso(usuario,contraseña,ingreso_usuario,ingreso_contraseña)

if acceso == True:
    entro = True
else:
    entro = False

while entro == True:
    print("----- a = Proyecto/b = Tablas/ c = Variables/ d = Mostrar/ e = Estadisticas/ f = Salir-----")
    menu = input("Bienvenido al programa ingrese su opcion: ")

    match menu:
            case "a":
                print("ingresaste a proyectos")
            case "b":
                print("ingresaste a tablas")
                tabla = crear_tabla()
                print(tabla)
                modificar = input("quere modifica la tabla si/no : ?")
                if modificar ==  "si":
                    modificar_tabla(tabla) 
                elif modificar == "no":
                    print("volviendo...")
            case "c":
                print("ingresaste a variables")
            case "d":
                print("ingresaste a mostrar")
                mostrar_tabla(tabla)   
            case "e":
                print("ingresaste a estadistica")
            case "f":
                print("saliendo....")
                entro = False
            case _:
                print("ingreso invalido")
