class Option:
    def __init__(self, msg, option_interface):
        self.msg = msg
        self.option_interface = option_interface

    def __repr__(self):
        return f"<Option {self.option_interface}>"


class Interface:
    def __init__(self, name, parent=None) -> None:
        self.name = name
        self.options_set = {}
        self.parent = parent

    def add_option(self, key, option):
        self.options_set[key] = option

    def add_back_option(self):
        if self.parent:
            self.add_option(0, Option("Back", self.parent))

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


# class Interface_v2:
#     def __init__(self, interface, parent_interface=None):
#         self.interface = interface
#         self.parent_interface = parent_interface
#         self.entry_point = parent_interface is None
#         self.default_option = {}
#         self.generated_options = {}

#         if self.entry_point is not True:
#             self.default_option[0] = 'Back option'

#         if (self.parent_interface and
#                 self.parent_interface.entry_point is not True):
#             self.default_option['*'] = 'Main menue'

#     def get_option_set(self):
#         return {**self.generated_options, **self.default_option}

#     def __repr__(self):
#         return (f"<[UI]: {self.interface}, "
#                 f"parent: {self.parent_interface}, "
#                 f"entry_point: {self.entry_point}, "
#                 f"options: {self.get_option_set()}>")


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


if __name__ == '__main__':
    # ui = Interface_v2('ui')
    # print(ui)
    # ui2 = Interface_v2('ui2', ui)
    # print(ui2)
    # ui3 = Interface_v2('ui3', ui2)
    # print(ui3)
    pass
