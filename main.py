from db.conexion import get_db_connection
from db.validaciones import validate_database_structure
from db.consultas import get_persons


def test_db_connection():
    conn = get_db_connection()
    print("Conexión exitosa a la base de datos")
    conn.close()


    

if __name__ == "__main__":
     # Paso 1: test conexión
    test_db_connection()
    
    # Paso 2: validar estructura
    validate_database_structure()

    # Paso 3: obtener personas
    get_persons()
