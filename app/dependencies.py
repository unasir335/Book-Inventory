from .models.database import SessionLocal

#manages database sessions for requests
def get_db():
    """Database session dependency"""
    db = SessionLocal()
    try:
        #let route handler handle session
        yield db
    finally:
        #close session
        db.close()