from .gs_reader import GSClientReader
from .import_data import create_collection, fill_collection


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

    def print_content(self):
        print(self.name)

    def get_user_responce(self):
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
        return user_response

    def execute_interface(self):
        self.print_content()
        user_response = self.get_user_responce()
        if user_response == 0:
            next_ui = self.default_options[0]
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


class GoogleSheetsInterface(Interface):
    def __init__(self, name, parent, new_table=False) -> None:
        Interface.__init__(self, name, parent)
        self.new_table = new_table
        self.table_content = []

    def execute_interface(self):
        self.print_content()
        if self.new_table:
            tab_link = input('Enter your tab link')
            print('connect to new table:\n', tab_link)
            gs_reader = GSClientReader(tab_link=tab_link)
        else:
            gs_reader = GSClientReader()

        ws_list = gs_reader.get_worksheets()
        for n, ws in enumerate(ws_list, 1):
            print(f"{n}. {ws.title}")

        while True:
            user_responce = int(input('select the option:\n'))
            if user_responce in range(1, (len(ws_list)+1)):
                break
            else:
                print('incorrect option, try again')

        self.table_content = gs_reader.get_ws_data(ws_list[user_responce-1])
        for n, data in enumerate(self.table_content, 1):
            print(f" - {n}. {data[0]}: {', '.join(data[1:])}")

        self.add_option(DBInterface('Save to...', parent=self))

        user_response = self.get_user_responce()

        if user_response == 0:
            next_ui = self.default_options[0]
        elif user_response == '-':
            next_ui = self.get_parent()
        else:
            next_ui = self.get_option(user_response)
        return next_ui


class DBInterface(Interface):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)

    def execute_interface(self):
        self.print_content()
        new_collection = Interface('Create new collection')
        exist_collection = Interface('Add to existing collection')
        self.add_option(new_collection, exist_collection)
        user_response = self.get_user_responce()
        if user_response == 0:
            next_ui = self.default_options[user_response]
        elif user_response == '-':
            next_ui = self.get_parent()
        elif user_response == 1:
            collection_name = input('Enter the name for the new collection:\n')
            create_collection(collection_name)
            fill_collection(collection_name, self.parent.table_content)
            next_ui = self.default_options[0]
        return next_ui


class DialogController:
    def __init__(self, main_interface):
        self.main_interface = main_interface

    def run_cli(self, ui):
        res_ui = ui.execute_interface()
        if res_ui.name == 'Main menue':
            res_ui = self.main_interface
        self.run_cli(res_ui)
