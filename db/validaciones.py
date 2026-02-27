from db.conexion import get_db_connection

#  Valida la estructura de la base de datos:
#  - Lista todas las tablas
#  - Lista las columnas y tipos de datos de cada tabla

def validate_database_structure():

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        print("\n=== VALIDANDO ESTRUCTURA DE BASE DE DATOS ===")

        # Obtener tablas
        cursor.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
        """)

        tablas = cursor.fetchall()

        if not tablas:
            print("No se encontraron tablas.")
            return

        for tabla in tablas:
            nombre_tabla = tabla[0]

            print(f"\nTabla: {nombre_tabla}")

            cursor.execute("""
                SELECT column_name, data_type
                FROM information_schema.columns
                WHERE table_name = %s
            """, (nombre_tabla,))

            columnas = cursor.fetchall()

            for col in columnas:
                print(f"   - {col[0]} ({col[1]})")

        print("\nValidación finalizada correctamente de tablas y columnas.")

    except Exception as e:
        print("Error validando estructura:", e)

    finally:
        cursor.close()
        conn.close()