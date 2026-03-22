from sqlalchemy.orm import Session
from model import Data
import datos

def get_data(db: Session):
    return db.query(Data).all()

def find_data(db:Session, data_id:int):
    return db.query(Data).filter(Data.id==data_id).first()

def create_data(db:Session, data:datos.data_create):
    db_data=Data(Temp=data.Temp,Humed=data.Humed)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def update_data(db:Session, data_id:int, data_update:datos.data_create):
    db_data=find_data(db,data_id)
    if db_data:
        db_data.Temp=data_update.Temp
        db_data.Humed=data_update.Humed
        db.commit()
        db.refresh(db_data)
        return db_data
    
def del_data(db:Session, data_id:int):
    db_data = find_data(db,data_id)
    if db_data:
        db.delete(db_data)
        db.commit()
        return db_data
