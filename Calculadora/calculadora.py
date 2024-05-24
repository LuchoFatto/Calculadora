from pack.funciones import *

def menu():
    print('''\na- Ingresar primer valor
b- Ingresar segundo valor
c- Operaciones
d- Mostrar Resultado
e- Salir\n''')
    return input("\nSeleccione una opcion del menu : \n")

def submenu():
    print('''\n1- Sumar
2- Restar
3- Dividir
4- Multiplicar
5- Factorial\n''')
    return

primer_paso = False
segundo_paso = False
tercer_paso = False

while True:
    match menu():
        case "a":
            numero_uno = validar_e_ingresar_numero()
            primer_paso = True
        case "b":
            if primer_paso:
                numero_dos = validar_e_ingresar_numero()
                segundo_paso = True
            else:
                print("\nDebe ingresar el primer valor\n")
        case "c":
            if segundo_paso:
                submenu()
                resultado = whileOpciones(numero_uno,numero_dos)
                tercer_paso = True
            else:
                print("\nDebe ingresar un valor primero\n")
        case "d":
            if tercer_paso:
                print(f"{resultado}")
                primer_paso = False
                segundo_paso = False
                tercer_paso = False
            elif segundo_paso:
                print("\nNo podes ver el resultado sin ingresar un operador\n")
            else:
                print("\nDebe ingresar un valor primero\n")
        case "e":
            break



