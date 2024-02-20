from __future__ import annotations


class CLInterface:
    pass


class ChatStory:
    storage = []


class Interface:
    def __init__(self, message) -> None:
        self.message = message
        self.answer_options = {}

    def add_answer(self, key, option):
        self.answer_options[key] = option

    def print_interface(self):
        print(self.message)
        for n, option in self.answer_options.items():
            print(f"{n}. {option}")

    def cli_requesrt(self):
        while True:
            result = input("select the option:\n")
            if result.isdigit():
                result = int(result)
            if result in self.answer_options:
                break
            else:
                print('incorrect option, try again')
        print('NICE!')


if __name__ == '__main__':
    i1 = Interface('Google Sheets')
    i1.add_answer(1, 'Display sheets from default table')
    i1.add_answer(2, 'Connect to table')
    i1.add_answer(0, 'Back')
    i1.add_answer('*', 'Main menu')
    i1.print_interface()
    i1.cli_requesrt()
