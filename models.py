from pydantic import BaseModel

class Books(BaseModel):
    title  : str
    author : str 
    price: float
    in_stock: bool