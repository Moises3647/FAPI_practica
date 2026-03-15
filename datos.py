from  pydantic import BaseModel

class Producto_create(BaseModel):
        id: int
        Nombre: str
        precio: float

class Producto_response(BaseModel):
        id: int
        Nombre: str
        precio: float


