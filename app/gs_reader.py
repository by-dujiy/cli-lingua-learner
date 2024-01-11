import gspread


class GSReader:
    def __init__(self, sa_file, tab_key):
        self.sa_file = sa_file
        self.tab_key = tab_key

    def get_ws_list(self):
        gs = gspread.service_account(self.sa_file)
        sh = gs.open_by_key(self.tab_key)
        return sh.worksheets()

    def get_gs_data(self, ws_id):
        gs = gspread.service_account(self.sa_file)
        sh = gs.open_by_key(self.tab_key)
        ws = sh.get_worksheet_by_id(ws_id)
        return ws.get_all_values()
