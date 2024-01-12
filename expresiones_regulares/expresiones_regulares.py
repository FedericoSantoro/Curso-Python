import re

texto = '''Hola, Como estas genio? Me llamo Fede y esta es la linea 1. 
Esta es la segunda (2) linea de texto
Y esta es la tercera ultima (3) y final (3) linea de texto'''

# Busca cadena de texto
resultado = re.search("Hola", texto)

# Busca todas las coincidencias
# resultado =  re.findall("esta", texto, flags = re.IGNORECASE) # Esto lo hace no case sensitive
resultado =  re.findall("esta", texto)

# \d --> busca digitos numericos del [0-9]
resultado =  re.findall(r"\d", texto)

# \D --> busca todo menos digitos numericos del [0-9]
resultado =  re.findall(r"\D", texto)

# \w --> busca caracteres alfanumericos [a-z A-Z 0-9 _]
resultado =  re.findall(r"\w", texto)

# \W --> busca todo menos caracteres alfanumericos [a-z A-Z 0-9 _]
resultado =  re.findall(r"\W", texto)

# \s --> busca espacios en blanco ( espacios, tabs y salto de linea)
resultado =  re.findall(r"\s", texto)

# \S --> busca todo menos espacios en blanco ( espacios, tabs y salto de linea)
resultado =  re.findall(r"\S", texto)

# \n --> busca saltos en linea
resultado =  re.findall(r"\n", texto)

# . --> busca todo menos saltos en linea
resultado =  re.findall(r".", texto)

# \ --> cancelar caracteres especiales, osea buscar un caracter especial especifico ( son los que no son alfanumericos [a-z A-Z 0-9 _] )
resultado =  re.findall(r"\,", texto)

# Armando cadena que busque numeros seguido de texto seguido de un punto y un espacio
resultado = re.findall(r"\d\.\s", texto)

# ^ --> busca el comienzo de una linea ( buscando Hola al principio de una linea )
# Con re.M convertimos al texto multilinea para que lo tenga en cuenta cada linea como una nueva
resultado = re.findall(r"^Hola", texto, flags = re.M)

# $ --> Busca el final de una linea ( buscando linea 1.  al principio de una linea )
resultado = re.findall(r"linea 1. $", texto, flags = re.M)

# {n} --> busca n cantidad de veces el valor de la izquierda
resultado =  re.findall(r"\w{3}", texto)

# {n, m} --> busca al menos n y como maximo m cantidad de veces
resultado =  re.findall(r"\w{3,4}", texto)

# (algo) --> busca un grupo junto, se puede combinar con el de {n}
resultado =  re.findall(r"ho{3}", texto) # Aca busca " hooo "
resultado =  re.findall(r"(ho){3}", texto) # Aca busca " hohoho "

# [algo] --> busca cualquier patron de lo que tenga dentro al combinarlo con {n}
resultado =  re.findall(r"[ho]{2}", texto) # Aca busca " ho, hh, oo, oh "

# | --> busca lo que esta a la izquierda o a la derecha
resultado =  re.findall(r"\d{1,3}|Hola", texto)

# * --> cuantificador para 0 o mas ocurrencias
resultado =  re.findall(r".*", texto)

# + --> cuantificador para 1 o mas ocurrencias
resultado =  re.findall(r".+", texto)

print(resultado)