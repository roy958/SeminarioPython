def OnlyLetterAndNumbers(char):
  if char.isdigit():
     return True
  elif char.isalpha():
     return True
  else:
     return False
char = input("faasda").strip()
if OnlyLetterAndNumbers(char):
     print("verdadero")
else:
     print("false")
