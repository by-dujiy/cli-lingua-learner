import os
import gspread
from typing import List
from dotenv import load_dotenv


load_dotenv()

GSA_FILE = os.environ.get('GSA_FILE_NAME')
TAB_KEY = os.environ.get('TAB_KEY')


class GSClientReader:
    def __init__(self, sa_file=GSA_FILE, tab_key=TAB_KEY):
        """
        Initializes a Google Spreadsheet instance
        Create connection with Google Spreadsheet by key of the Google Sheets
        tab

        :param sa_file: Name of the service account file.
        :param tab_key: The key of the Google Spreadsheet
        """
        self.client = sa_file
        self.tab_key = tab_key
        self.gs = gspread.service_account(self.client)
        self.sh = self.gs.open_by_key(self.tab_key)

    def get_ws_list(self) -> List[gspread.Worksheet]:
        """
        Get a list of all worksheets in the spreadsheet

        :return: List of gspread.Worksheet objects.
        """
        return self.sh.worksheets()

    def get_gs_data(self, worksheet: gspread.Worksheet) -> List[List[str]]:
        """
        Get data from a particular worksheet.

        :param worksheet: the worksheet object.
        :return: A list of lists containing the data
        """
        ws = self.sh.get_worksheet_by_id(worksheet.id)
        return ws.get_all_values()
