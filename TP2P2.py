titles = [
"Speedrun de Super Mario en tiempo récord",
"Charla sobre desarrollo de videojuegos",
"Jugando al nuevo FPS del momento con amigos",
"Música en vivo: improvisaciones al piano"
]
max = 0
titumax = ""
for titulos in titles:
    aux = len(titulos)
    if aux > max:
        max = aux
        titumax = titulos
print(" el titulo mas largo es: ")
print(titumax)# como lo concateno con lo demas?
      