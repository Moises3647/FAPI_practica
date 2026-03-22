from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import model, datos
import data.crud as crud
from database import SessionLocal,engine

model.Base.metadata.create_all(bind=engine)

app=FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/data/{data_id}', response_model=datos.data_responce)
def get_data(data_id,db:Session = Depends(get_db)):
      db_data = crud.find_data(db,data_id)
      if db_data is None:
            raise HTTPException(status_code=404, detail="No existe el data")
      return db_data
@app.get('/data', response_model=list[datos.data_responce])
def get_all_data(db:Session = Depends(get_db)):
        data= crud.get_data(db)
        return data

@app.post('/data', response_model=datos.data_responce)
def crear_data(data: datos.data_create, db:Session = Depends(get_db)):
        return crud.create_data(db,data=data)

@app.put('/data/{data_id}',response_model=datos.data_create)
def actualizar_data(data_id:int, data:datos.data_create,db:Session=Depends(get_db)):
      data_db=crud.update_data(db,data_id,data)
      if data_db is None:
            raise HTTPException(status_code=404, detail="No existe el data")
      return data_db

@app.delete('/data/{data_id}',response_model=datos.data_responce)
def eliminar_data(data_id:int,db:Session=Depends(get_db)):
      data_db=crud.del_data(db,data_id)
      if data_db is None:
            raise HTTPException(status_code=404, detail="No existe el data")
      return data_db    
