from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import model, datos
import productos.crud as crud
from database import SessionLocal,engine

model.Base.metadata.create_all(bind=engine)

app=FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/productos/{producto_id}', response_model=datos.Producto_response)
def get_product(producto_id,db:Session = Depends(get_db)):
      db_producto = crud.find_product(db,producto_id)
      if db_producto is None:
            raise HTTPException(status_code=404, detail="No existe el producto")
      return db_producto
@app.get('/productos', response_model=list[datos.Producto_response])
def get_all_productos(db:Session = Depends(get_db)):
        productos= crud.get_products(db)
        return productos

@app.post('/productos', response_model=datos.Producto_response)
def crear_producto(producto: datos.Producto_create, db:Session = Depends(get_db)):
        return crud.create_product(db,producto=producto)

@app.put('/productos/{producto_id}',response_model=datos.Producto_create)
def actualizar_producto(producto_id:int, producto:datos.Producto_create,db:Session=Depends(get_db)):
      producto_db=crud.update_product(db,producto_id,producto)
      if producto_db is None:
            raise HTTPException(status_code=404, detail="No existe el producto")
      return producto_db

@app.delete('/productos/{producto_id}',response_model=datos.Producto_response)
def eliminar_producto(producto_id:int,db:Session=Depends(get_db)):
      producto_db=crud.del_product(db,producto_id)
      if producto_db is None:
            raise HTTPException(status_code=404, detail="No existe el producto")
      return producto_db    
