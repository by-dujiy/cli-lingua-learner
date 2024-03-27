from dotenv import load_dotenv
from app import Interface, DialogController, GoogleSheetsInterface
from app import fill_db

load_dotenv()


main_menu = Interface('Main menu', entry_point=True)
download_new = Interface('Download new')
display_available = Interface('Display available')
excel_menu = Interface('Ecxel')
load_file = Interface('Load file')
google_sheets = Interface('Google Sheets')
default_table = GoogleSheetsInterface('Display default table',
                                      parent=google_sheets)
connect_new = Interface('Connect to new table')


main_menu.add_option(download_new, display_available)
download_new.add_option(google_sheets, excel_menu)
excel_menu.add_option(load_file)
google_sheets.add_option(default_table, connect_new)


if __name__ == "__main__":
    fill_db()
    dc = DialogController(main_menu)
    dc.run_cli(main_menu)
