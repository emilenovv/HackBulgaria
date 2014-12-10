from base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Projection(Base):
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    movies = relationship("Movie", backref="projections")
    type = Column(String)
    date = Column(String)
    time = Column(String)

    def __str__(self):
        return "[{}] - {} {} ({})".format(self.id, self.date, self.time, self.type)

    def __repr__(self):
        return self.__str__()
