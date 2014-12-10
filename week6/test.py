from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship


Base = declarative_base()


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __str__(self):
        return "{} - {}".format(self.id, self.name)

    def __repr__(self):
        return self.__str__()


class Grade(Base):
    __tablename__ = "grade"
    id = Column(Integer, primary_key=True)
    value = Column(Float)
    student_id = Column(Integer, ForeignKey("student.id"))
    student = relationship("Student", backref="grades")


engine = create_engine("sqlite:///university.db")
Base.metadata.create_all(engine)

session = Session(bind=engine)

session.add_all([
    Student(name="Rado", age=23),
    Student(name="Ivo", age=21),
    Student(name="Ivan", age=23)])


rado = session.query(Student).filter(Student.name == "Rado").one()

rado.grades = [Grade(value=6), Grade(value=5), Grade(value=3)]
session.commit()



