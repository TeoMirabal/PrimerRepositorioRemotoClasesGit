from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
# URL DE LA BASE DE DATOS
DATABASE_PASSWORD = os.getenv("DB_PASSWORD")
DATABASE_URL = f"mysql+pymysql://root:{DATABASE_PASSWORD}@localhost:3306/clase1"
# Crear el otor de la base de datos
engine = create_engine(DATABASE_URL, echo=True)

# Clase base para definir los modelos

Base = declarative_base()

# COnfiguracion de la sesion
SessionLocal = sessionmaker(autoflush=False, bind=engine)
