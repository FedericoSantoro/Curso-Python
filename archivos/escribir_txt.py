with open("archivos\\texto.txt", "w", encoding = "UTF-8") as archivo:
    # Sobreescribe el archivo
    # archivo.write("Nuevo texto")
    # Sobreescribe el archivo, pero al agregar mas writelines se acumulan y escribe todo
    archivo.writelines(["Nuevo texto\n", "Otro nuevo texto para otra linea"])