from database import engine, Base
from models import User
from sqlalchemy.orm import sessionmaker

# Crear las tablas en la base de datos -> Introducir usuarios
if __name__ == "__main__":
    print("Insertando usuario en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("Base de datos lista!")
    try:
        print("Insertando datos..")
        # COnfiguracion de la sesion
        SessionLocal = sessionmaker(autoflush=False, bind=engine)
        db = SessionLocal()

        new_user = User(name="raquel", age=20)

        # Agregar el usuario como una fila
        db.add(new_user)
        db.commit()
        print("Usuario insertado con exito")
    except Exception as e:
        db.rollback()
        print("El usuario no pudo ser ingresado...")
