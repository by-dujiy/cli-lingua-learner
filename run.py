from dotenv import load_dotenv
from app.cli_interface import Interface, DialogController, GSInterface
from app import GSClientReader

load_dotenv()

gsr = GSClientReader()


main_menu = Interface('Main menu', entry_point=True)
download_new = Interface('Download new')
display_available = Interface('Display available')
excel_menu = Interface('Ecxel')
load_file = Interface('Load file')
google_sheets = Interface('Google Sheets')
default_table = GSInterface('Display default table',
                            func=gsr.get_ws_list,
                            parent=google_sheets,
                            proc_func=gsr.get_ws_data)
default_table.add_option()
connect_new = Interface('Connect to new table')


main_menu.add_option(download_new, display_available)
download_new.add_option(google_sheets, excel_menu)
excel_menu.add_option(load_file)
google_sheets.add_option(default_table, connect_new)


if __name__ == "__main__":
    dc = DialogController(main_menu)
    dc.run_cli(main_menu)
    # x = gsr.get_ws_list()
    # b = gsr.get_ws_data(x[0])
    # for i in b:
    #     print(i)
