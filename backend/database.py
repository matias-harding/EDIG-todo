from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import cryptography


# MySQL configuration
username = 'edig'
password = '3dig_t0D0'
hostname = 'localhost:3307'
database_name = 'EDIG_TODO'

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{username}:{password}@{hostname}/{database_name}"

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    # Attempt to connect to the database
    connection = engine.connect()
    connection.close()  # Close the connection after checking
    print(">>>> Successfully connected to MySQL!")
except Exception as e:
    print(f">>>> Failed to connect to MySQL: {e}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
