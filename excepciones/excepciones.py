def suma():
    while True:
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        try:
            resultado = int (a) + int (b)
        except ValueError as e:
            print("Datos incorrectos")
            print(f"Error: {e}")
        except ZeroDivisionError as e:
            print("Division por 0 no valida")
            print(f"Error: {e}")
        else:
            break
        finally:
            print("Se ejecuta siempre")
    return resultado

print(suma())