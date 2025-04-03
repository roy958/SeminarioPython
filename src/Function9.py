def eliminarRepetidos(list,name):
   encontre = False
   for word in list:
     if word == name:
      encontre = True
   return encontre
def analizarDatos(clientes):
    list = []
    for cliente in clientes:
       if cliente and cliente.strip():
        clientee = cliente.strip()
        clientee = clientee.title()
        repet = eliminarRepetidos(list,clientee)
        if repet == False:
          list.append(clientee)
    return list