from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(Integer, default=1)

    def __repr__(self):
        return f'Player (id = {self.id}, name = {self.name}, level = {self.level})'
