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

from os import system
from time import sleep
from scripts.data_manager import Scrape, Update, Verify, Sort
from scripts.grapher import Graph
from scripts.ui_manager import UIHandler
from scripts.ui_manager import InputHandler

# ================================================
#                Define Constants
# ================================================

ui = UIHandler()
inp = InputHandler(ui)
sort = Sort()

# ================================================
#                Define Functions
# ================================================


def main():
    # ===========================
    #  *        INFO
    #   Menu loop, user controlled
    # ===========================
    ui.print_menu()
    menuChoice = inp.get_choice_input(
        "Please select a menu option (1-99): ", ["1", "2,", "3", "4", "5", "99"])
    if menuChoice == "1":
        Graph(InputHandler(ui).get_data_status_input())
    elif menuChoice == "2":
        Update()
    elif menuChoice == "3":
        Verify()
    elif menuChoice == "4":
        sort.sort(InputHandler(ui).get_data_status_input())
    elif menuChoice == "5":
        Scrape()
    elif menuChoice == "99":
        ui.success("Closing program...")
        ui.reset()
        exit(0)
    inp.get_continue_input("Press enter to continue.")


# ===========================
#        DRIVER CODE
# ===========================
if __name__ == '__main__':
    try:
        sleep(1)
        while True:
            system('clear')
            main()
    except KeyboardInterrupt:
        ui.error('\nKeyboard Interrupt (Ctrl+C) detected. Exiting...')
        ui.reset()
        exit(0)
