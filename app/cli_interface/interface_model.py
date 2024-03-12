class Interface:
    def __init__(self, name, func=None, parent=None, entry_point=False):
        self.name = name
        self.func = func
        self.entry_point = entry_point
        self.parent = parent
        self.option_count = 1
        self.default_options = {}
        self.additional_options = {}

    def add_option(self, *options):
        for n, option in enumerate(options, 1):
            self.additional_options[n] = option

        if self.parent:
            self.default_options['-'] = Interface('Back')
            if not self.parent.entry_point:
                self.default_options[0] = Interface('Main menue')

    def option_set(self):
        return {**self.additional_options, **self.default_options}

    def get_parent(self):
        return self.parent

    def get_option(self, key):
        return self.additional_options[key]

    def __repr__(self):
        return (f"<Interface '{self.name}', func: {self.func}, entry_point: "
                f" {self.entry_point}, parent: "
                f"[{self.parent.name if self.parent else None}]> "
                f"additional_optionals: {self.additional_options}"
                f"default_options: {self.default_options}")


class DialogController:
    def __init__(self, main_interface):
        self.main_interface = main_interface
        self.back_option = None
        self.go_main_option = None

    def execute_interface(self, ui):
        print(ui.name)
        for key, option in ui.option_set().items():
            print(key, option.name)

        while True:
            user_response = input('select the option:\n')
            if user_response.isdigit():
                user_response = int(user_response)
            if user_response in ui.option_set():
                break
            else:
                print('incorrect option, try again')

        if user_response == 0:
            next_ui = self.main_interface
        elif user_response == '-':
            next_ui = ui.get_parent()
        else:
            next_ui = ui.get_option(user_response)
        return next_ui

    def run_cli(self, ui):
        ui.func() if ui.func else None
        res_ui = self.execute_interface(ui)
        self.run_cli(res_ui)