from db import Model
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class WordsPair(Model):
    __tablename__ = 'wordspair'

    id: Mapped[int] = mapped_column(primary_key=True)
    word: Mapped[str] = mapped_column(String(64), nullable=False)

    translations = relationship('Translation', back_populates='word_pair')


class Translation(Model):
    __tablename__ = 'translation'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    translation_word: Mapped[str] = mapped_column(String(64), nullable=False)
    word_pair_id: Mapped[int] = mapped_column(Integer,
                                              ForeignKey('wordspair.id'),
                                              nullable=False)

    word_pair = relationship("WordsPair", back_populates='translations')
