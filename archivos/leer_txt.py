# El encoding es para usar caracteres con coma por ej
archivo_sin_leer = open("archivos\\texto.txt", encoding = "UTF-8")

# Leer archivo completo
# archivo = archivo_sin_leer.read()

#Leer linea por linea
# linea = archivo_sin_leer.readlines()

# Leer una sola linea
linea_1 = archivo_sin_leer.readline()

# Cerrar archivo
archivo_sin_leer.close()

print(linea_1)