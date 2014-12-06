from sqlalchemy import Column, String, Integer
from base import Base


class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)

    def __str__(self):
        return "{} - {}".format(self.name, self.score)

    def __repr__(self):
        return self.__str__()


