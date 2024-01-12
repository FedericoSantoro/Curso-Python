# Creando excepcion
class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"El error es: {err}")

# Ejecuntado excepcion
try:
    # Throw Error
    raise MiExcepcion("ERROR ENCONTRADO")
except MiExcepcion as e:
    print("Encontre un error")