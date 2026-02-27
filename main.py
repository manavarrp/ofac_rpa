from db.conexion import get_db_connection
from db.validaciones import validate_database_structure
from db.consultas import get_persons, get_results, delete_results
from bot.proceso_ofac import separar_registros_masivos, insertar_masivos


def test_db_connection():
    conn = get_db_connection()
    print("Conexión exitosa a la base de datos")
    conn.close()


if __name__ == "__main__":
     # Paso 1: test conexión
     #test_db_connection()
    
    # Paso 2: validar estructura
    validate_database_structure()

    # Paso 3: obtener personas
    persons = get_persons()

    # Paso 5: separar registros masivos
    masivo, completos = separar_registros_masivos(persons)

    # Paso 5: Insertar resultados masivos
    insertar_masivos(masivo) 

    get_results()

    #delete_results()

 

