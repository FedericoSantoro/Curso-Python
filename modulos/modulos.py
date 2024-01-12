# Dos metodos de importar modulos

# Importando modulo y nombrandolo m_saludar, sus funciones deben ser usadas como metodos
import modulo_saludar as m_saludar

# Eligiendo que funciones importar y renombrandolas, para elegir todas se puede usar el *, no recomendado el *
from modulo_saludar import Saludar as primer_saludo, Saludar2 as segundo_saludo

# Importando de otra carpeta
from funciones_buenas.modulo_con_funciones import Otro_saludo

segundo_saludo("Maria")
m_saludar.saludar("Jose")
Otro_saludo("Miriam")