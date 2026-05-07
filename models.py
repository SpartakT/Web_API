from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Exchanger(Base):
    __tablename__ = "exchangers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    rate = Column(Float)
    reserve = Column(Float)
    reviews = Column(Integer)
    min_btc = Column(Float)
    max_btc = Column(Float)