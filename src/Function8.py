import random
import string
    
def descuento(nombre,fecha):
    longitud = len(nombre) + len(fecha)
    longitud = longitud - 30
    caracteres = string.ascii_letters + string.digits  
    cadenaRandom= ''.join(random.choice(caracteres) for _ in range(15))
    nombre = nombre.upper()
    cadenaRandom = cadenaRandom.upper()
    dia,mes,anio = fecha.split("-")
    fecha = dia + mes + anios
    cadena = f"{nombre}-{fecha}-{cadenaRandom}"
    return cadena