import this
def esvocal (frase):
    frase = frase.lower()
    palabra = frase[1]
    if palabra[0] in 'aeiou':
        return True
    else:
        return False

zenText = """Colocar aquí el Zen de Python"""
for frase in zenText:
    if esvocal(frase) == True:
        print(frase) # no se que esta mal