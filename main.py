# ===========================================================================
#  ?                                ABOUT
#  @author         : Nathan Hines
#  @email          : nathan@hines.net.nz
#  @repo           : https://github.com/zerrissen/kiwigrapher
#  @description    : Main user UI, program entry point.
# ===========================================================================

# ================================================
#                Define Imports
# ================================================


from scripts.data_manager import Scrape, Update, Verify, Sort
from scripts.grapher import Graph


# ================================================
#                Define Functions
# ================================================


def main():
    print('Kiwigrapher - ASB Kiwisaver Funds Grapher')
    print('Version: 1.1.0\n')

    # ===========================
    #  *        INFO
    #   Menu loop, user controlled
    # ===========================
    print(f'1\tView Data\t\tDisplays line graph of all data')
    print(f'2\tUpdate Existing Data\t\tUpdates existing data from last saved date')
    print(f'3\tVerify Existing Data\t\tChecks for anomolous/missing data and corrects it')
    print(f'4\tSort Existing Data\t\tSplits existing data by Kiwisaver Fund')
    print(f'5\tScrape New Data\t\tScrapes a full new set of data from ASB.')
    print(f'99\tExit Program  ')
    while True:
        try:
            menuChoice = int(input('\nPlease select a menu option (1-99): '))
        except ValueError:
            print('Error: Please enter a valid number.')
            continue
        break
    if menuChoice == 1:
        Graph(getType())
    elif menuChoice == 2:
        Update()
    elif menuChoice == 3:
        Verify()
    elif menuChoice == 4:
        Sort(getType())
    elif menuChoice == 5:
        Scrape()
    elif menuChoice == 99:
        exit(0)

# ================================================
#  *                  getType
#  ? Allows the user to select between verified & unverified data
#  ? Used to determine some functionality.
#  @ param None
#  @ return string
# ================================================


def getType():
    print(f'\t\t1\tVerified Data')
    print(f'\t\t2\tUnverified Data')
    while True:
        try:
            typeChoice = int(
                input('Please select a verification option (1-2): '))
        except ValueError:
            print('Error: Please enter a valid number.')
            continue
        if typeChoice == 1:
            return 'verified'
        elif typeChoice == 2:
            print("Sorry, unfortunately, this option is currently not available.")
            return None
        else:
            print('Error: Invalid choice. Returning to menu.')
            return None


# ===========================
#        DRIVER CODE
# ===========================
if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('Keyboard Interrupt (Ctrl+C) detected. Exiting...')
        exit(0)
