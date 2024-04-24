temp=29

def WearJacketToday():
  temp=80
  print('temperature in func Jacket=',temp)
  if (temp < 40):
     return True
  return False

def WearHatToday():
  global temp
  temp = -5
  print('temperature in func Hat=',temp)
  if (temp < 40):
     return None
  return False

print('temperature before func=',temp)
print("Wear a Jacket Today? ",WearJacketToday())
print('temperature after func=',temp)
print("Wear a Hat Today?",WearHatToday())
print('temperature after func=',temp)
