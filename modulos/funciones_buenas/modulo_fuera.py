# Si esta fuera de la carpeta, en un nivel superior, se debe importar sys para ver el directorio y agregar el path con append de la
# carpeta de la cual se desea importar el modulo para posteriormente importarlo
import sys
sys.path.append('C:\\Users\\fechu\\Documents\\Programas\\cursoPython\\modulos')
from modulo_saludar import Saludar

Saludar("Pepe")