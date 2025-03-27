def contienecaracteres(nombre):
    if len(nombre) >= 5:
       print("es mayor")
       return True
    else: 
       return False
def contieneNum(caracter):
   if caracter.isdigit():
      return True
   else:
      return False
def contieneMayus(caracter):
    if caracter.isupper():
       return True
    else:
       return False
def OnlyLetterAndNumbers(char):
  if char.isalpha():
     return True
  elif char.isdigit():
     return True
def analizoNombre (nombre):
    mayus = False
    num = False
    cumple = True
    if contienecaracteres(nombre):
       for letter in nombre:
          if OnlyLetterAndNumbers(letter):
             if mayus == False:
                 if contieneMayus(letter):
                     mayus = True
             elif num == False:
                 if contieneNum(letter):
                     num = True
          else:
             print("que paso")
             cumple = False
             break
    else: 
         return False     
    if mayus == True & num == True & cumple == True :
          print("devuelve verdadero")
          return True
    else:
          return False 
Nombre = input ("ingrese un nombre de usuario").strip()
if analizoNombre(Nombre) == True: 
     print("el nombre es valido")
else:
    print("el nombre de usuario no cumple los requisitos")