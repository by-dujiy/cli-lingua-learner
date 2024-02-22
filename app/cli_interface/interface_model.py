class Option:
    def __init__(self, msg, option_interface):
        self.msg = msg
        self.option_interface = option_interface

    def __repr__(self):
        return f"<Option {self.option_interface}>"


class Interface:
    def __init__(self, name) -> None:
        self.name = name
        self.options_set = {}

    def add_option(self, key, option):
        self.options_set[key] = option

    def print_interface(self):
        print(self.name)
        for n, option in self.options_set.items():
            print(f"{n}. {option.msg}")

    def cli_request(self):
        while True:
            result = input("select the option:\n")
            if result.isdigit():
                result = int(result)
            if result in self.options_set:
                break
            else:
                print('incorrect option, try again')
        return result

    def __repr__(self):
        return f"<Interface '{self.name}'> option items:\n{self.options_set}"


class PerformInterface(Interface):
    def __init__(self, name, func):
        Interface.__init__(self, name)
        self.func = func

    def execute(self):
        self.func()

    def __repr__(self):
        return f"<PerformInterface '{self.name}'> func:{self.func.__name__}"


class DialogController:
    call_stack = []

    def __init__(self, ui_collection):
        self.ui_collection = ui_collection

    def execute_interface(self, ui):
        if ui.name == "Back":
            ui = self.prev_ui()

        ui.print_interface()
        if isinstance(ui, PerformInterface):
            ui.execute()
        res = ui.cli_request()
        self.call_stack.append(ui)
        self.execute_interface(ui.options_set[res].option_interface)

    def prev_ui(self):
        self.call_stack.pop()
        return self.call_stack.pop()

    def run_cli(self):
        self.execute_interface(self.ui_collection[0])
