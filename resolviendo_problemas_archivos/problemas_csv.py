# Cambiar tipo de dato de una columna
import pandas as pd
df = pd.read_csv("resolviendo_problemas_archivos\\datos.csv")

df["edad"] = df["edad"].astype(str)

# Reemplazar valor
df["apellido"].replace("dalto", "Lopez", inplace = True)

# Eliminando filas con datos nan
df = df.dropna()

# Eliminar columnas con datos faltantes
# df = df.dropna(axis = 1)

#Eliminando filas repetidas
df = df.drop_duplicates()

# Creando csv con dataframe limpio
df.to_csv("resolviendo_problemas_archivos\\datos_limpios.csv")
