def esta(frase,clave):
    esta = False
    for word in frase:
        if word == clave:
           esta = True
    return esta
def devolverfrase(rules , clave):
    devolver = " "
    rules = rules.split(".")
    for frase in rules:
       if esta(frase,clave) == True:
           devolver += frase + "  "
    return devolver

rules = """Respeta a los demás. No se permiten insultos ni lenguaje ofensivo.
Evita el spam. No publiques enlaces sospechosos o repetitivos.
No compartas información personal.
Usa los canales adecuados para cada tema.
Sigue las instrucciones de los moderadores."""
clave = input("ingrese una palabra clave")
print(devolverfrase(rules,clave))
print("a")# porque me devuelve vacia