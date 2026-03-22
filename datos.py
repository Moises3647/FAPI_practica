from  pydantic import BaseModel

class data_create(BaseModel):
        id: int
        Temp: float
        Humed: float

class data_responce(BaseModel):
        id: int
        Temp: float
        Humed: float


