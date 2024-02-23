# interface_model.py
class Option:
    def __init__(self, msg, option_interface):
        """Initializes an option with a message and the interface to navigate to."""
        self.msg = msg
        self.option_interface = option_interface

    def __repr__(self):
        return f"<Option {self.option_interface}>"

class Interface:
    def __init__(self, name, parent=None):
        """Initializes an interface with a name and optional parent interface."""
        self.name = name
        self.options_set = {}
        self.parent = parent

    def add_option(self, key, option):
        """Adds an option to the interface."""
        self.options_set[key] = option

    def print_interface(self):
        """Prints the interface and its options."""
        print(self.name)
        for n, option in self.options_set.items():
            print(f"{n}. {option.msg}")

    def cli_request(self):
        """Handles user input for selecting an option."""
        while True:
            result = input("Select the option:\n")
            if result.isdigit():
                result = int(result)
            if result in self.options_set:
                break
            else:
                print('Incorrect option, try again')
        return result

    def __repr__(self):
        return f"<Interface '{self.name}'> option items:\n{self.options_set}"

class PerformInterface(Interface):
    def __init__(self, name, func, parent=None):
        """Initializes a performing interface with a function to execute."""
        super().__init__(name, parent)
        self.func = func

    def execute(self):
        """Executes the associated function."""
        self.func()

    def __repr__(self):
        return f"<PerformInterface '{self.name}'> func:{self.func.__name__}"

class DialogController:
    def __init__(self, ui_collection):
        """Initializes the dialog controller with a collection of interfaces."""
        self.ui_collection = ui_collection

    def execute_interface(self, ui):
        """Executes the given interface and manages the navigation."""
        ui.print_interface()

        if isinstance(ui, PerformInterface):
            ui.execute()

        res = ui.cli_request()

        if res == 0 and ui.parent:
            self.execute_interface(ui.parent)
        else:
            self.execute_interface(ui.options_set[res].option_interface)

    def run_cli(self):
        """Runs the CLI application."""
        self.execute_interface(self.ui_collection[0])

# ui.py
import interface_model as im

def mock_func():
    print("Something's going on.")

main_menu = im.Interface("MAIN MENU")
download_new = im.Interface("Download new", main_menu)
display_available = im.PerformInterface("Display available...", mock_func, main_menu)
google_sheets = im.Interface("Google Sheets", download_new)
excel = im.Interface("Excel", download_new)
