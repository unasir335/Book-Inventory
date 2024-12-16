"""
Pydantic models for request/response validation
"""
from pydantic import BaseModel, Field, constr
from typing import Optional
from datetime import datetime

class BookBase(BaseModel):
    """Base Pydantic model for Book"""
    title: constr(min_length=1, max_length=100)
    author: constr(min_length=1, max_length=100)
    publish_year: int = Field(..., gt=1000, lt=9999)
    isbn: constr(min_length=13, max_length=13)
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0)

class BookCreate(BookBase):
    """Pydantic model for creating a new book"""
    pass

class BookUpdate(BaseModel):
    """Pydantic model for updating a book"""
    title: Optional[constr(min_length=1, max_length=100)] = None
    author: Optional[constr(min_length=1, max_length=100)] = None
    publish_year: Optional[int] = Field(None, gt=1000, lt=9999)
    price: Optional[float] = Field(None, gt=0)
    quantity: Optional[int] = Field(None, ge=0)

class Book(BookBase):
    """Pydantic model for book response"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True