class InputHandler:
    def __init__(self, ui_handler):
        self.ui = ui_handler

    def get_input(self, prompt):
        return input(prompt)

    def get_continue_input(self, prompt):
        while True:
            try:
                choice = input(prompt)
                return choice
            except ValueError:
                self.ui.error("Error: Invalid input.")

    def get_int_input(self, prompt):
        while True:
            try:
                num = int(input(self.ui.prompt(prompt)))
                return num
            except ValueError:
                self.ui.error("Error: Please enter a valid integer.")

    def get_float_input(self, prompt):
        while True:
            try:
                num = float(input(self.ui.prompt(prompt)))
                return num
            except ValueError:
                self.ui.error("Error: Please enter a valid float.")

    def get_choice_input(self, prompt, choices):
        while True:
            try:
                choice = input(self.ui.prompt(prompt)).lower()
                if choice in [x.lower() for x in choices]:
                    print('-'*37)
                    return choice
                else:
                    raise ValueError
            except ValueError:
                self.ui.error("Error: Please enter a valid choice.")

    def get_yes_no_input(self, prompt):
        while True:
            try:
                choice = input(self.ui.prompt(prompt)).lower()
                if choice == "yes" or choice == "y":
                    return True
                elif choice == "no" or choice == "n":
                    return False
                else:
                    raise ValueError
            except ValueError:
                self.ui.error("Error: Please enter a valid choice.")

    def get_data_status_input(self):
        self.ui.printVerificationChoice()
        while True:
            try:
                choice = int(
                    input(f'\n{self.ui.prompt("Please select a verification option(1-2): ")}'))
                print('\n')
            except ValueError:
                self.ui.error('Error: Please enter a valid number.')
                continue
            if choice == 1:
                self.ui.warning(
                    "Sorry, unfortunately, this option is currently not available.")
                return None
            elif choice == 2:
                return 'unverified'
            else:
                self.ui.error('Error: Invalid choice. Returning to menu.')
                return None
