from gs_reader import GSClientReader
from db import Model, engine
# from models import WordsPair, Translation


def download_from_gs():
    reader = GSClientReader()
    ws_list = reader.get_ws_list()
    return reader.get_gs_data(ws_list[3])


def fill_db():
    Model.metadata.drop_all(engine)
    Model.metadata.create_all(engine)

    # input_data = download_from_gs()
