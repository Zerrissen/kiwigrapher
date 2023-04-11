# ===========================================================================
#  ?                                ABOUT
#  @author         : Nathan Hines
#  @email          : nathan@hines.net.nz
#  @repo           : https://github.com/zerrissen/kiwigrapher
#  @description    : Program entry point. Handles user input.
# ===========================================================================

# ================================================
#                Define Imports
# ================================================

from scripts.data_manager import Scrape, Update, Verify, Sort
from scripts.grapher import Graph
from scripts.ui_manager import UIHandler
from scripts.ui_manager import InputHandler

# ================================================
#                Define Constants
# ================================================

ui = UIHandler()

# ================================================
#                Define Functions
# ================================================


def main():
    # ===========================
    #  *        INFO
    #   Menu loop, user controlled
    # ===========================
    ui.printMenu()
    menuChoice = InputHandler.get_choice_input(
        "Please select a menu option (1-99): ", ["1", "2,", "3", "4", "5", "99"])
    if menuChoice == "1":
        Graph(getType())
    elif menuChoice == "2":
        Update()
    elif menuChoice == "3":
        Verify()
    elif menuChoice == "4":
        Sort(getType())
    elif menuChoice == "5":
        Scrape()
    elif menuChoice == "99":
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
    InputHandler.get_data_status_input()


# ===========================
#        DRIVER CODE
# ===========================
if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        ui.error('Keyboard Interrupt (Ctrl+C) detected. Exiting...')
        exit(0)
