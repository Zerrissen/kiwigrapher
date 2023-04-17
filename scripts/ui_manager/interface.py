from colorama import Fore, Style
from .. import Fore, Style, just_fix_windows_console, init, load, os, randint, AnsiToWin32


class UIHandler:
    def __init__(self):
        just_fix_windows_console()

    def success(self, message):
        print(Fore.GREEN + Style.NORMAL + message)

    def error(self, message):
        print(Fore.RED + Style.BRIGHT + message)

    def warning(self, message):
        print(Fore.YELLOW + Style.NORMAL + message)

    def reset(self):
        print(Style.RESET_ALL)

    def plus(self, message):
        print(
            f'{Fore.WHITE}{Style.NORMAL}[{Fore.GREEN}+{Fore.WHITE}] ' + message)

    def minus(self, message):
        print(
            f'{Fore.WHITE}{Style.NORMAL}[{Fore.RED}-{Fore.WHITE}] ' + message)

    def prompt(self, message):
        return f'{Fore.BLUE}{Style.BRIGHT}{message}{Style.RESET_ALL}'

    def print_menu(self):
        title_id = str(randint(1, 3))
        # Open the file containing the titles
        with open('scripts\\\\ui_manager\\\\assets\\\\titles.json', 'r') as f:
            # Load the titles from the file into a list
            titles = load(f)['titles']

        # Print each title in color
        title = next((t for t in titles if t['id'] == title_id), None)
        if title:
            for line in title["content"]:
                print(line)

        print(f'{Fore.WHITE}{Style.BRIGHT}\nKiwigrapher - ASB Kiwisaver Funds Grapher')
        print(f'{Fore.WHITE}Version: {Style.NORMAL}{Fore.GREEN}1.1.0{Style.RESET_ALL}')
        print('-'*14+'\n')
        print(
            f'[1] {Style.BRIGHT}View Data{Style.NORMAL}{"Displays line graph of all data":>50}')
        print(
            f'[2] {Style.BRIGHT}Update Existing Data\t{Style.NORMAL}{"Updates existing data from last saved date":<50}')
        print(
            f'[3] {Style.BRIGHT}Verify Existing Data\t{Style.NORMAL}{"Checks for anomolous/missing data and corrects it":<50}')
        print(
            f'[4] {Style.BRIGHT}Sort Existing Data\t{Style.NORMAL}{"Splits existing data by Kiwisaver Fund":>46}')
        print(
            f'[5] {Style.BRIGHT}Scrape New Data\t{Style.NORMAL}{"Scrapes a full new set of data from ASB.":>48}')
        print(f'[99] {Fore.YELLOW}Exit Program{Style.RESET_ALL}\n')

    def print_verification_choice(self):
        print("\nDo you want to operate with verified or unverified data?")
        print(f'\t[1] {Style.BRIGHT}Verified Data{Style.NORMAL}')
        print(f'\t[2] {Style.BRIGHT}Unverified Data{Style.RESET_ALL}')
