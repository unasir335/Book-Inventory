from fastapi import FastAPI
from app.routes import book
from app.models.database import engine
from app.models.book import Base

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI application
app = FastAPI(
    title="Book Management System",
    description="A FastAPI application for managing books",
    version="1.0.0"
)

# Include routers
app.include_router(book.router, tags=["books"])