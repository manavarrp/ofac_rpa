from db.conexion import get_db_connection

def test_db_connection():
    conn = get_db_connection()
    print("Conexión exitosa a la base de datos")
    conn.close()

if __name__ == "__main__":
    test_db_connection()