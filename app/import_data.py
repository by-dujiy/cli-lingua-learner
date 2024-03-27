from .db import Session, Model, engine
from .models import WordsPair, Translation, Collection
from psycopg2.errors import UniqueViolation
from sqlalchemy import select


session = Session()


def fill_db():
    """
    Drop exist tables and create new tables in db
    """
    print('Dropping tables...')
    Model.metadata.drop_all(engine)
    print('Creating tables...')
    Model.metadata.create_all(engine)


def create_collection(name):
    """
    Create new collection in db
    """
    with Session() as session:
        with session.begin():
            try:
                c = Collection(name=name)
                session.add(c)
                print(f"Collection '{name} created")
            except UniqueViolation:
                session.rollback()
                print(f"Collection named '{name}' already exist!")


def fill_collection(collection_name, content):
    with Session() as session:
        with session.begin():
            c = session.scalar(select(Collection)
                               .where(Collection.name == collection_name))
            for row in content:
                wp = WordsPair(word=row.pop(0))
                c.wordspairs.append(wp)
                for item in row:
                    t = Translation(translation_word=item)
                    wp.translations.append(t)
