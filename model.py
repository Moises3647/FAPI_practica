from sqlalchemy import Column,Integer,String,Float
from  database import Base

class Data(Base):
    __tablename__="Data"
    id = Column(Integer, primary_key=True, index=True)
    Temp = Column(Float)
    Humed = Column(Float)

