import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("resolviendo_problemas_graficos\\pedos.csv")

# Creando el grafico
sns.lineplot(x = "fecha", y = "pedos", data = df)

# Creando un punto en el mayor punto
plt.plot("01-09", 17, "o")

# Mostrando el grafico
plt.show()

