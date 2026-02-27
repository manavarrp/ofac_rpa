from db.conexion import get_db_connection

# Función para obtener todas las personas de la base de datos
def get_persons():
    conn = cursor= None  

    try: 
        conn = get_db_connection()
        cursor = conn.cursor()
        # Consulta SQL para obtener personas con su dirección y país (si existen)
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

        print("\nDatos obtenidos de la base de datos:")
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



# Función para obtener los resultados de la tabla Resultadosuser4105
def get_results():
    conn = cursor= None

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            SELECT *
            FROM "Resultadosuser4105"
        """

        cursor.execute(query)
        results = cursor.fetchall()

        print("\nDatos obtenidos de la base de datos:")
        for row in results:
            print(row)

        return results
    
    except Exception as e:
        print(f"Error al obtener personas: {e}")
        return []
    
    finally:
        cursor.close()
        conn.close()

# Inserta registros en la tabla Resultadosuser4105
def insert_results_bulk(registros):
    if not registros:
        print("No hay registros para insertar.")
        return

    conn = cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Obtener idPersona ya existentes
        cursor.execute('SELECT "idPersona" FROM "Resultadosuser4105"')
        existentes = {row[0] for row in cursor.fetchall()}

        # Filtrar registros nuevos
        nuevos = [r for r in registros if r[0] not in existentes]
        if not nuevos:
            print("\nNo hay registros nuevos para insertar.")
            return

        # Insertar registros nuevos
        sql = """
            INSERT INTO "Resultadosuser4105"
            ("idPersona", "nombrePersona", "pais", "cantidadDeResultados", "estadoTransaccion")
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.executemany(sql, nuevos)
        conn.commit()
        print(f"\n{len(nuevos)} registros masivos insertados.")

    except Exception as e:
        print(f"Error insertando registros: {e}")
        if conn:
            conn.rollback()
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
   
#  Elimina todos los registros de la tabla Resultadosuser4105 a modo de limpieza para nuevas pruebas
def delete_results():
    """
    Elimina todos los registros de la tabla Resultadosuser4105.
    """
    conn = cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = 'DELETE FROM "Resultadosuser4105"'
        cursor.execute(sql)
        conn.commit()
        print("Todos los registros eliminados de Resultadosuser4105.")

    except Exception as e:
        print(f"Error eliminando registros: {e}")
        if conn: conn.rollback()

    finally:
        if cursor: cursor.close()
        if conn: conn.close()