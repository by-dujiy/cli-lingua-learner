from .db import Model
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Collection(Model):
    __tablename__ = 'collections'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64), index=True, unique=True)

    wordspairs: Mapped[list['WordsPair']] = relationship(
        cascade='all, delete-orphan', back_populates='collection')

    def __repr__(self):
        return f"Collection({self.id}, '{self.name}')"


class WordsPair(Model):
    __tablename__ = 'wordspairs'

    id: Mapped[int] = mapped_column(primary_key=True)
    word: Mapped[str] = mapped_column(String(64), unique=True)
    collection_id: Mapped[int] = mapped_column(
        ForeignKey('collections.id'), index=True)

    collection: Mapped['Collection'] = relationship(
        back_populates='wordspairs')

    translations: Mapped[list['Translation']] = relationship(
        cascade='all, delete-orphan', back_populates='wordspair')

    def __repr__(self):
        return f"WordsPair({self.id}, '{self.word}')"


class Translation(Model):
    __tablename__ = 'translations'

    id: Mapped[int] = mapped_column(primary_key=True)
    translation_word: Mapped[str] = mapped_column(String(64), nullable=False)
    wordspair_id: Mapped[int] = mapped_column(
        ForeignKey('wordspairs.id'), index=True)

    wordspair: Mapped['WordsPair'] = relationship(
        back_populates='translations')

    def __repr__(self):
        return f"Translation({self.id}, '{self.translation_word}')"
