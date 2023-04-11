from .. import Fore, Style, just_fix_windows_console, init


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
            f"{Fore.WHITE}{Style.NORMAL}[{Fore.GREEN}+{Fore.WHITE}] " + message)

    def minus(self, message):
        print(
            f"{Fore.WHITE}{Style.NORMAL}[{Fore.RED}-{Fore.WHITE}] " + message)

    def printMenu(self):
        print('Kiwigrapher - ASB Kiwisaver Funds Grapher')
        print('Version: 1.1.0\n')
        print(f'1\tView Data\t\tDisplays line graph of all data')
        print(f'2\tUpdate Existing Data\t\tUpdates existing data from last saved date')
        print(
            f'3\tVerify Existing Data\t\tChecks for anomolous/missing data and corrects it')
        print(f'4\tSort Existing Data\t\tSplits existing data by Kiwisaver Fund')
        print(f'5\tScrape New Data\t\tScrapes a full new set of data from ASB.')
        print(f'99\tExit Program')

    def printVerificationChoice(self):
        print(f'\t\t1\tVerified Data')
        print(f'\t\t2\tUnverified Data')
