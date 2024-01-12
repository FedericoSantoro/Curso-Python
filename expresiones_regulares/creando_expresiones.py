# Detectando un numero CABA y ocultandolo
import re

texto = "Hola Pedro, mi numero es: +54 11 4321-4321"

pattern = r"\+\d{2}\s\d{2}\s[0-9-]{8,9}"

new_text = re.sub(pattern, "(Numero Oculto)", texto)

print(new_text)