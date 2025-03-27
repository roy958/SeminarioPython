def clasificacionTime(time):
    if time < 200: 
      print("rapido")
    elif 200 < time & time < 500:
       print("normal")
    else:
       print("Lento")
time = int(input("ingrese su tiempo de reaccion en el juego"))
clasificacionTime(time)       