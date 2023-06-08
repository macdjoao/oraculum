from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(Integer, default=1)
    race = Column(Integer, ForeignKey('races.id'))

    def __repr__(self):
        return f'Players (id = {self.id}, name = {self.name}, level = {self.level})'


class Race(Base):
    __tablename__ = 'races'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f'Races (id = {self.id}, name = {self.name})'
