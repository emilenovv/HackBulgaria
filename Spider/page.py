from sqlalchemy import Column, Integer, String
from base import Base


class Page(Base):
    __tablename__ = "pages"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    url = Column(String)
