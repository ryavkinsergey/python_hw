import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://postgres:123456@localhost:5432/postgres"

Base = declarative_base()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)


@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(engine)
    session = Session()
    yield session
    session.close()


def test_add_student(db_session):
    new_student = Student(name="Ivan Test")
    db_session.add(new_student)
    db_session.commit()

    student = db_session.query(Student).filter_by(name="Ivan Test").first()
    assert student is not None

    db_session.delete(student)
    db_session.commit()


def test_update_student(db_session):
    student = Student(name="Update Me")
    db_session.add(student)
    db_session.commit()

    student.name = "Updated Name"
    db_session.commit()

    updated = db_session.query(Student).filter_by(id=student.id).first()
    assert updated.name == "Updated Name"

    db_session.delete(updated)
    db_session.commit()


def test_delete_student(db_session):
    student = Student(name="To Be Deleted")
    db_session.add(student)
    db_session.commit()

    db_session.delete(student)
    db_session.commit()

    result = db_session.query(Student).filter_by(name="To Be Deleted").first()
    assert result is None
