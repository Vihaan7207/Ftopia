# ASCII Generator: https://fsymbols.com/generators/carty/
from helpers.colors import fg, util
from helpers.snippets import prompts
from helpers.functions import typePrint
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
typePrint(f'{fg.green}{util.bold}You have just arrived in this world, and you will embark on an amazing journey in the days to come{util.reset}')