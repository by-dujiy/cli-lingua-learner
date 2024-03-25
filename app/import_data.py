from db import Session, Model, engine
from models import WordsPair, Translation, Collection


session = Session()


def fill_db():
    Model.metadata.drop_all(engine)
    Model.metadata.create_all(engine)

    # input_data = download_from_gs()


def create_collection(name):
    session.add(Collection(name=name))
