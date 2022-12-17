import sys, time
from helpers.colors import fg, util
def typePrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  
def typeInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value

def printChoices(imagery, choices):
  print(imagery)
  for i in range(len(choices)):
    print(f'[{i+1}] {choices[i]}')