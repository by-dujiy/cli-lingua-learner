import interface_model as im

main_menu = im.Interface("MAIN MENU")
download_new = im.Interface("Download new")
display_available = im.Interface("Display available")
back = im.Interface("Back")
google_sheets = im.Interface("Google Sheets")
excel = im.Interface("Excel")
load_file = im.Interface("Load file")
available_colletions = im.Interface("List of available collections...")
default_table = im.Interface("Display default table...")
connect_new = im.Interface("Connect to new table...")
table_list_content = im.Interface("List of sheets from table")


main_menu.add_option(1, im.Option("Download new collection", download_new))
main_menu.add_option(2, im.Option("Display available collection",
                                  display_available))

download_new.add_option(1, im.Option("Google Sheets", google_sheets))
download_new.add_option(2, im.Option("Excel", excel))
download_new.add_option(0, im.Option("Back", back))

display_available.add_option(1, im.Option(
    "Display list of available collections", available_colletions))
display_available.add_option(0, im.Option("Back", back))

google_sheets.add_option(1, im.Option("Display sheets from default table",
                                      default_table))
google_sheets.add_option(2, im.Option("Connect to new table", connect_new))
google_sheets.add_option(0, im.Option("Back", back))
google_sheets.add_option('*', im.Option("Main menu", main_menu))

excel.add_option(1, im.Option("Load file", load_file))
excel.add_option(0, im.Option("Back", back))
excel.add_option('*', im.Option("Main menu", main_menu))

# table_list_content.add_option()


def prev_ui():
    pass


if __name__ == '__main__':
    ls = [1, 2, 3, 4]
    ls.pop()
    print(ls)
    print(ls.pop())
