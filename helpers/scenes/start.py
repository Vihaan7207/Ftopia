import helpers.scenes.first_choice_mountains 
import helpers.scenes.first_choice_plains 
import helpers.scenes.village_entrance
from helpers.functions import printChoices

def main():
    printChoices('You find yourself in a grass plain. To the north is a village. To the west is mountains. To the south and east there are more plains.\nDo you want to:', ['Go to the village', 'Go to the mountains', 'Explore the plains'])
    choice = input('> ')
    if choice == '1':
        helpers.scenes.village_entrance.main()
    elif choice == '2':
        helpers.scenes.first_choice_mountains.main()
    elif choice == '3':
        helpers.scenes.first_choice_plains.main()