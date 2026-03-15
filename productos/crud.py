from sqlalchemy.orm import Session
from model import Producto
import datos

def get_products(db: Session):
    return db.query(Producto).all()

def find_product(db:Session, product_id:int):
    return db.query(Producto).filter(Producto.id==product_id).first()

def create_product(db:Session, producto:datos.Producto_create):
    db_producto=Producto(Nombre=producto.Nombre,precio=producto.precio)
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def update_product(db:Session, product_id:int, product_update:datos.Producto_create):
    db_producto=find_product(db,product_id)
    if db_producto:
        db_producto.Nombre=product_update.Nombre
        db_producto.precio=product_update.precio
        db.commit()
        db.refresh(db_producto)
        return db_producto
    
def del_product(db:Session, product_id:int):
    db_producto = find_product(db,product_id)
    if db_producto:
        db.delete(db_producto)
        db.commit()
        return db_producto
