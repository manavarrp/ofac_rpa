from db.conexion import get_db_connection

# Función para obtener todas las personas de la base de datos
def get_persons():
    conn = None
    cursor = None   

    try: 
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = """
            SELECT
                p."idPersona",
                p."nombrePersona",
                m."direccion",
                m."pais"
            FROM "Personas" p
            LEFT JOIN "MaestraDetallePersonas" m
                ON p."idPersona" = m."idPersona"
            WHERE p."aConsultar" = 'Si'
        """

        cursor.execute(query)
        results = cursor.fetchall()

        print("Datos obtenidos de la base de datos:")
        for row in results:
            print(row)

        return results
    
    except Exception as e:
        print(f"Error al obtener personas: {e}")
        return []
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()





