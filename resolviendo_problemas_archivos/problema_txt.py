# 2 listas, una con nombres otra con apellidos

nombres = ["Lucas", "Matias", "Camila", "Pedro", "Roberto"]
apellidos = ["Dalto", "Zing", "Dalto", "Robetix", "Lopez"]

# Registrar info en txt optimamente
with open("resolviendo_problemas_archivos\\nombres_y_apellidos.txt", "w") as archivo:
    archivo.writelines('"nombre","apellido"\n')
    [archivo.writelines(f'"{nombre}","{apellido}"\n') for nombre,apellido in zip(nombres,apellidos)]