import os
import gspread
from typing import List
from dotenv import load_dotenv


load_dotenv()

GSA_FILE = os.environ.get('GSA_FILE_NAME')
TAB_LINK = os.environ.get('TAB_LINK')


class GSClientReader:
    def __init__(self, sa_file=GSA_FILE, tab_link=TAB_LINK):
        """
        Initializes a Google Spreadsheet instance
        Create connection with Google Spreadsheet by key of the Google Sheets
        tab

        :param sa_file: Name of the service account file.
        :param tab_key: The key of the Google Spreadsheet
        """
        self.client = sa_file
        self.tab_link = tab_link
        self.gs = gspread.service_account(self.client)
        self.sh = self.gs.open_by_url(self.tab_link)

    def get_worksheets(self) -> List[gspread.Worksheet]:
        """
        Get a list of all worksheets in the spreadsheet

        :return: List of gspread.Worksheet objects.
        """
        return self.sh.worksheets()

    def get_ws_data(self,
                    worksheet: gspread.Worksheet,
                    delimiter=',') -> List[List[str]]:
        """
        Get data from a particular worksheet.

        :param worksheet: the worksheet object.
        :return: A list of lists containing the data
        """
        print('connecting to', worksheet.title)
        ws = self.sh.get_worksheet_by_id(worksheet.id)
        result = []
        for item in ws.get_all_values():
            buffer_list = []
            for sub_item in item:
                if sub_item:
                    if delimiter in sub_item:
                        units = sub_item.split(delimiter)
                        for unit in units:
                            buffer_list.append(unit.strip().lower())
                    else:
                        buffer_list.append(sub_item)
            result.append(buffer_list)
        return result
