# Creando procedimiento simple
def saludar():
    print("Hola, Soy Fede")
    
saludar()

# Creando procedimiento con parametros
def saludar_a(persona, sexo):
    sexo = sexo.lower()
    if sexo == "mujer":
        print(f"Hola reina, Como estas {persona}?")
    elif sexo == "hombre":
        print(f"Hola rey, Como estas {persona}?")
    else:
        print(f"Hola fiera, Como estas {persona}?")
        
saludar_a("Fede", "Hombre")

# Creando una funcion
def crear_contrasena(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contrasena = f"{chars[c1]}{chars[c2]}{chars[c3]}{num_entero*2}"
    return contrasena
    
crear_contrasena(98)
    