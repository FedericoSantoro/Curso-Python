import pandas as pd

# Data frame ( parecido a hoja de calculo, tiene filas y columnas) y le agregamos nombres a las columnas con " names "
# df = pd.read_csv("archivos\\datos.csv", names = ["name", "lastname", "age"])
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

# Obteniendo datos de columna nombre
nombres = df["nombre"]


# Tecnica slicing, antes de los " : " se pone donde comienza y despues hasta donde termina ( uno anterior), por defecto si esta vacio recorre todo
# cadena = "0123456789"
# print(cadena[:])

# Ordenar los datos por edad por ej
df_ordenado_ascendente = df.sort_values(by = "edad")

# Ordenandolo de forma descendente
df_ordenado_descendente = df.sort_values(by = "edad", ascending = False)

# Concatenando dos df
df_concatenado = pd.concat([df, df2])

# Accediendo a las primeras filas con head()
primeras_filas = df.head(3)

# Accediendo a las ultimas filas con tail()
ultimas_filas = df.tail(3)

# Para saber cuantas columnas y filas hay se usa shape

filas_totales, columnas_totales = df.shape

# Obteniendo data estadistica del df
df_info = df.describe()

# Accediendo a elemento especifico con loc ( edad de la fila 2 )
elemento_especifico_loc = df.loc[2, "edad"]

# Accediendo a elemento especifico con iloc por indice ( edad de la fila 2 )
elemento_especifico_iloc = df.iloc[2, 2]

# Accediendo a todas las filas de una columna ( apellidos con loc )
apellidos = df.loc[ : , "apellido"]

# Accediendo a todas las filas de una columna ( apellidos con iloc )
apellidos = df.iloc[ : , 1]

# Accediendo a la fila 3 con loc y iloc
fila_3_loc = df.loc[2, : ]
fila_3_iloc = df.iloc[2, : ]

# Accediendo a filas con edad mayor que 30
mayor_que_30 = df.loc[df["edad"]>30, : ]

print(mayor_que_30)