def validar_e_ingresar_numero()-> int:
    while True:
        try:
            numero = int(input("Ingrese un numero : "))
            return numero
        except ValueError:
            print("ERROR debe ingresar un numero : ")

def suma(valor_uno: int, valor_dos: int)-> int:
    suma = valor_uno + valor_dos
    return f"El resultado de A+B es: {suma}"

def resta(valor_uno: int, valor_dos: int)-> int:
    resta = valor_uno - valor_dos
    return f"El resultado de A-B es: {resta}"

def dividir(valor_uno: int, valor_dos: int)-> float:
    if valor_dos == 0:
        return "No es posible dividir por cero"
    else:
        division = valor_uno / valor_dos
        return f"El resultado de A/B es: {division}"

def multiplicar(valor_uno: int, valor_dos: int)-> int:
    multiplicacion = valor_uno * valor_dos
    return f"El resultado de A*B es: {multiplicacion}"

def factorial(numero: int)-> int:
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

def factorial_dos_nuemros(valor_uno: int, valor_dos: int)-> int:
    primero = factorial(valor_uno)
    segundo = factorial(valor_dos)
    return f"El factorial de A es: {primero} y El factorial de B es: {segundo}"

def whileOpciones(valor_uno: int, valor_dos: int):
    while True:
        opcion = input("\nIngrese un opcion : \n")
        match opcion.lower():
            case "sumar" | "1":
                return suma(valor_uno,valor_dos)
            case "restar" | "2":
                return resta(valor_uno,valor_dos)
            case "dividir" | "3":
                return dividir(valor_uno,valor_dos)
            case "multiplicar" | "4":
                return multiplicar(valor_uno,valor_dos)
            case "factorial" | "5":
                return factorial_dos_nuemros(valor_uno, valor_dos)
