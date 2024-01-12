# Al terminar el bloque se cierra automaticamente
with open("archivos\\texto.txt", encoding = "UTF-8") as archivo:
    contenido = archivo.read()
    print(contenido)