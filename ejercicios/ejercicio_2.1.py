def nueva_persona():
    nombre = input("Introduzca el nombre de la persona: ")
    edad = int(input("Introduzca la edad de la persona: "))
    return (nombre, edad)

def anotar_asistencia(cantidad_asistencia):
    asistencia = []
    for _ in range(cantidad_asistencia):
        asistencia = [*asistencia, nueva_persona()]
    asistencia.sort(key = lambda dato : dato[1])
    asistente = asistencia[0][0]
    profesor = asistencia [-1][0]
    return asistente, profesor

asistente, profesor = anotar_asistencia(3)
print(f"El profesor es {profesor} y el asistente es {asistente}")