class Interface:
    def __init__(self,
                 name,
                 func=None,
                 parent=None,
                 entry_point=False,
                 content_module=None):
        self.name = name
        self.func = func
        self.entry_point = entry_point
        self.parent = parent
        self.content_module = content_module
        self.default_options = {}
        self.additional_options = {}

    def add_option(self, *options):
        for n, option in enumerate(options, 1):
            option.set_parent(self)
            self.additional_options[n] = option

        if self.parent:
            self.default_options['-'] = Interface('Back')
            if not self.parent.entry_point:
                self.default_options[0] = Interface('Main menue')

    def get_option_set(self):
        return {**self.additional_options, **self.default_options}

    def set_parent(self, parent_interface):
        self.parent = parent_interface

    def get_parent(self):
        return self.parent

    def get_option(self, key):
        return self.additional_options[key]

    def execute_interface(self):
        print(self.name)
        for key, option in self.get_option_set().items():
            print(key, option.name)

        while True:
            user_response = input('select the option:\n')
            if user_response.isdigit():
                user_response = int(user_response)
            if user_response in self.get_option_set():
                break
            else:
                print('incorrect option, try again')

        if user_response == 0:
            next_ui = self.main_interface
        elif user_response == '-':
            next_ui = self.get_parent()
        else:
            next_ui = self.get_option(user_response)
        return next_ui

    def __repr__(self):
        return (f"<Interface '{self.name}', func: {self.func}, entry_point: "
                f" {self.entry_point}, parent: "
                f"[{self.parent.name if self.parent else None}]> "
                f"additional_optionals: {self.additional_options}"
                f"default_options: {self.default_options}")


class GSInterface(Interface):
    def __init__(self, name, func, parent, proc_func=None):
        Interface.__init__(self, name, func, parent=parent)
        self.proc_func = proc_func

    def add_option(self):
        options = []
        ws_list = self.func()
        for ws in ws_list:
            options.append(Interface(ws.title, content_module=ws))
        return super().add_option(*options)

    def get_content(self, worksheet):
        res = self.proc_func(worksheet)
        for item in res:
            print(item)

    def execute_interface(self):
        print(self.name)
        for key, option in self.get_option_set().items():
            print(key, option.name)

        while True:
            user_response = input('select the option:\n')
            if user_response.isdigit():
                user_response = int(user_response)
            if user_response in self.get_option_set():
                break
            else:
                print('incorrect option, try again')

        if user_response == 0:
            next_ui = self.main_interface
        elif user_response == '-':
            next_ui = self.get_parent()
        else:
            user_ws = self.get_option(user_response)
            self.get_content(user_ws.content_module)
            next_ui = Interface('Save collection', parent=self)
            next_ui.add_option()
        return next_ui


class DialogController:
    def __init__(self, main_interface):
        self.main_interface = main_interface

    def run_cli(self, ui):
        res_ui = ui.execute_interface()
        self.run_cli(res_ui)
