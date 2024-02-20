import os
import app
import config
from dotenv import load_dotenv


load_dotenv()


def download_from_gs():

    def print_gs_content(gs_list):
        ws_num = 0
        for n, ws in enumerate(gs_list):
            print(f"{n}. {ws.title}: {ws.id}")
            ws_num = n

        print("Select one from the available list of sheets:")
        user_input = get_user_chouse(0, ws_num)
        return reader.get_gs_data(ws_list[user_input])

    print("...loading data...")
    tab_key = os.getenv('TAB_KEY')
    reader = app.GSClientReader(config.GSA_FILE, tab_key)
    ws_list = reader.get_ws_list()
    responce = print_gs_content(ws_list)
    for item in responce:
        print(item)

    print("""
          1. Load current data in database\n
          2. Show available list of sheets again\n""")


def processing_googlesh():
    print("1. Connect default table\n2. Connect a new table")
    user_choice = get_user_chouse(1, 2)
    if user_choice == 1:
        download_from_gs()
    elif user_choice == 2:
        connect_new_gsh()


def connect_new_gsh():
    print("Add google bot in your table and Enter 'tab key'...")


def get_user_chouse(*valid_options):
    while True:
        user_input = int(input("Enter your option: "))
        if user_input in valid_options:
            return user_input
        print("Invalid option, please try again.")


def main_swich():
    print('1. Download new data')
    print('2. Display available collection')
    user_choice = get_user_chouse(1, 2)
    if user_choice == 1:
        print('Where do we load the data from?')
        print('1. Google Sheets')
        print('2. Excel')
        user_choice = get_user_chouse(1, 2)
        if user_choice == 1:
            print("Download from Google Sheets...")
            processing_googlesh()
        elif user_choice == 2:
            print("Download from Excel...")
    elif user_choice == 2:
        print('Display available collection...')


if __name__ == "__main__":
    main_swich()
