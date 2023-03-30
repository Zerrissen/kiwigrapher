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
            menuChoice = int(input('Please select a menu option (1-99): '))
        except ValueError:
            print('Error: Please enter a valid number.')
            continue
        break
    if menuChoice == 1:
        Graph()
    elif menuChoice == 2:
        Update()
    elif menuChoice == 3:
        Verify()
    elif menuChoice == 4:
        Sort()
    elif menuChoice == 5:
        Scrape()
    elif menuChoice == 99:
        exit(0)


if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('Keyboard Interrupt (Ctrl+C) detected. Exiting...')
        exit(0)
