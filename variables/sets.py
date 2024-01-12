# Creando conjunto con set()
# Un set puede tener una tupla dentro pero no lista o diccionario
conjunto = set(["Dato1", ("Dato2", "Dato3")])

# Conjunto dentro de otro conjunto
conjunto1 = frozenset(["Dato1", "Dato2"])
conjunto2 = {conjunto1, "Dato3"}

print(conjunto2)

# Teoria Conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

# Verificando si es subconjunto
resultado1 = conjunto2.issubset(conjunto1)
resultado2 = conjunto2 <= conjunto1

print(resultado1)
print(resultado2)

# Verificando si es superconjunto
resultado11 = conjunto2.issuperset(conjunto1)
resultado21 = conjunto2 < conjunto1

print(resultado11)
print(resultado21)

# Verificar si no tienen ningun numero en comun
resultado3 = conjunto2.isdisjoint(conjunto1)

print(resultado3)