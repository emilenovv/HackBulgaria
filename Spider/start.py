from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from crawler import Crawler
from base import Base


def main():
    engine = create_engine("sqlite:///search.db")
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    my_crawler = Crawler('boredpanda.com', session)
    my_crawler.scan_website()

if __name__ == '__main__':
    main()





