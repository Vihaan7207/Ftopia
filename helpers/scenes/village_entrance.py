from helpers.functions import printChoices
from helpers.colors import fg
import helpers.scenes.start

def main():
    printChoices('You walk to the entrance to the village. There is a gate with two guards.\nYou can:', ['Ask the guards to enter', 'Look for a different entrance', 'Go back'])
    choice = input('> ')
    if choice == '3':
        helpers.scenes.start.main()
