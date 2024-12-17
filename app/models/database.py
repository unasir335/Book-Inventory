"""
Database connection configuration and base model
"""
# database.py handles database connection and session management
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

# Create database engine, maintains the connection poo
engine = create_engine(DATABASE_URL)

# Create SessionLocal class for database sessions, used to create new database sessions for each request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class for database models
#all database models inherit from this base
Base = declarative_base()
