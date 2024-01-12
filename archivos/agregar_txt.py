# Con la "a" se hace append, se agrega a lo que estaba previamente
with open("archivos\\texto.txt", "a", encoding = "UTF-8") as archivo:
    # Agregando el archivo
    archivo.write("Nuevo texto con append\n")