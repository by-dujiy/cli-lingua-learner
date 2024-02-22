import interface_model as im


def mock_func():
    print("something's going on")


main_menu = im.Interface("MAIN MENU")
download_new = im.Interface("Download new")
display_available = im.PerformInterface("Display available...", mock_func)
back = im.Interface("Back")
google_sheets = im.Interface("Google Sheets")
excel = im.Interface("Excel")
load_file = im.PerformInterface("Load file...", mock_func)
available_colletions = im.PerformInterface("List of available collections...",
                                           mock_func)
default_table = im.PerformInterface("Display default table...",
                                    mock_func)
connect_new = im.PerformInterface("Connect to new table...",
                                  mock_func)
table_list_content = im.PerformInterface("List of sheets from table",
                                         mock_func)


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

interface_collection = [
    main_menu,
    download_new,
    display_available,
    back,
    google_sheets,
    excel,
    load_file,
    available_colletions,
    default_table,
    connect_new,
    table_list_content]

if __name__ == '__main__':
    cli = im.DialogController(interface_collection)
    cli.run_cli()
