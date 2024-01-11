import os

import app
import config
from dotenv import load_dotenv


load_dotenv()

tab_key = os.getenv('TAB_KEY')
reader = app.GSClientReader(config.GSA_FILE, tab_key)


if __name__ == "__main__":
    ws_list = reader.get_ws_list()
    for ws in ws_list:
        print(f"{ws.title}: {ws.id}")

    print(reader.get_gs_data(ws_list[2]))
