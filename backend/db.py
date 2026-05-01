from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///data.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    skin_type = Column(String)
    symptoms = Column(String)
    diagnosis = Column(String)
    routine = Column(String)

Base.metadata.create_all(engine)
