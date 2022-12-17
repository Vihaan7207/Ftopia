# ASCII Generator: https://fsymbols.com/generators/carty/
from helpers.colors import fg, util
from helpers.snippets import prompts
from helpers.functions import typePrint, printChoices
import helpers.scenes.village_entrance, helpers.scenes.first_choice_mountains, helpers.scenes.first_choice_plains
print(util.clear)
print(f'''{fg.blue}{util.bold}
███████╗████████╗░█████╗░██████╗░██╗░█████╗░
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║██╔══██╗
█████╗░░░░░██║░░░██║░░██║██████╔╝██║███████║
██╔══╝░░░░░██║░░░██║░░██║██╔═══╝░██║██╔══██║
██║░░░░░░░░██║░░░╚█████╔╝██║░░░░░██║██║░░██║
╚═╝░░░░░░░░╚═╝░░░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝{util.reset}''')
input(prompts.enter)
typePrint(f'{fg.green}{util.bold}Welcome to Ftopia, a magical land full of mystical wonders\n{util.reset}')
input(prompts.enter)
typePrint(f'{fg.green}{util.bold}You have just arrived in this world, and you will embark on an amazing journey in the days to come\n{util.reset}')
input(prompts.enter)
print(util.clear)
printChoices('You find yourself in a grass plain. To the north is a village. To the west is mountains. To the south and east there are more plains.\nDo you want to:', ['Go to the village', 'Go to the mountains', 'Explore the plains'])
choice = input('> ')
if choice == '1':
    helpers.scenes.village_entrance.main()
elif choice == '2':
    helpers.scenes.first_choice_mountains.main()
elif choice == '3':
    helpers.scenes.first_choice_plains.main()