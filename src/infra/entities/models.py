from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Player(Base):
    __tablename__ = 'players'

    name = Column(String, primary_key=True)
    level = Column(Integer, default=1)
    race = Column(String, ForeignKey('races.name'))
    grade = Column(String, ForeignKey('grades.name'))

    def __repr__(self):
        return f'Player (name = {self.name}, level = {self.level}, race = {self.race}, grade = {self.grade})'


class Race(Base):
    __tablename__ = 'races'

    name = Column(String, primary_key=True)

    def __repr__(self):
        return f'Race (name = {self.name})'


class Grade(Base):
    __tablename__ = 'grades'

    name = Column(String, primary_key=True)

    def __repr__(self):
        return f'Grade (name = {self.name})'
