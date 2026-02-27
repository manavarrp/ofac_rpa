import psycopg2
from config import DATABASE_URL

# Función para establecer la conexión a la base de datos
def get_db_connection():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        raise 