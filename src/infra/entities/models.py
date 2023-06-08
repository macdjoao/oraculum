from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(Integer, default=1)
    race = Column(Integer, ForeignKey('races.id'))
    grade = Column(Integer, ForeignKey('grades.id'))

    def __repr__(self):
        return f'Player (id = {self.id}, name = {self.name}, level = {self.level}, race = {self.race}, grade = {self.grade})'


class Race(Base):
    __tablename__ = 'races'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f'Race (id = {self.id}, name = {self.name})'


class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f'Grade (id = {self.id}, name = {self.name})'
