
from pydantic.v1 import BaseModel, Field, validator, root_validator, EmailStr
from typing import List


class Product(BaseModel):
    id: str = Field(regex='^[A-Za-z0-9-]*$')
    name: str
    category: str
    price: int
    quantity_in_stock: int

    @validator('price', 'quantity_in_stock')
    def results(cls, value: int) -> int:
        if value < 50:
            raise ValueError('Error')
        return value


class OrderItem(BaseModel):
    product: Product
    quantity: int


class Order(BaseModel):
    id: str = Field(regex='^[A-Za-z0-9-]*$')
    order_date: str
    customer_id: str
    items: List[OrderItem]
    status: str


class Customer(BaseModel):
    id: str = Field(regex='^[A-Za-z0-9-]*$')
    name: str
    email: EmailStr

    @validator('email')
    def email(cls, value):
        if not value.endswith('@email.com'):
            raise ValueError('Error')
        return value
