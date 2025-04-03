def imprimirOrdenado (resultados):
    resultados_dict = resultados[0]
    ordenado = sorted(resultados_dict.items(), key=lambda x: x[1]['puntos'], reverse=True)
    for jugador, stats in ordenado:
       print(f"{jugador}: {stats}")  

def modificarResultados(resultados,kills,asistencia,muerte,j,lista,total):
     resultados[0][lista[j]]['kills'] += kills
     resultados[0][lista[j]]['assists'] +=  asistencia
     if muerte == True:
         resultados[0][lista[j]]['deaths'] += 1
     resultados[0][lista[j]]['puntos'] +=  total
     return resultados

def analizarRounds(rounds,resultados):
   list = ['Shadow','Blaze','Viper','Frost','Reaper']
   for i in range(5) :
      mvp = 0
      for j in range(5):
         kills = rounds[i][list[j]]['kills']
         asistencia = rounds[i][list[j]]['assists']
         muerte = rounds[i][list[j]]['deaths']
         total = (kills * 3) + asistencia
         if (muerte == True):
              total = total - 1
         resultados = modificarResultados(resultados,kills,asistencia,muerte,j,list,total)
         if (total > mvp):
            mvp = total
            who = j
      resultados[0][list[who]]['MVPs'] += 1
      print (f"ronda: {i + 1}" )
      imprimirOrdenado(resultados)
      print(f"el MVP en esta ronda es: {list[who]}")
      print()
   return resultados   

