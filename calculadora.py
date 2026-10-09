
# Operaciones
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


# Calculadora en consola
def main():
    print("=== CALCULADORA BASICA ===")

    num1 = float(input("Primer numero: "))
    num2 = float(input("Segundo numero: "))

    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        print("Resultado:", add(num1, num2))
    elif opcion == "2":
        print("Resultado:", sub(num1, num2))
    elif opcion == "3":
        print("Resultado:", mul(num1, num2))
    elif opcion == "4":
        try:
            print("Resultado:", div(num1, num2))
        except ValueError as error:
            print("Error:", error)
    else:
        print("Opcion no valida")


if __name__ == "__main__":
    main()
