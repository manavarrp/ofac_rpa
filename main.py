from db.conexion import get_db_connection
from db.validaciones import validate_database_structure
from db.consultas import get_persons, get_results, delete_results
from bot.proceso_ofac import split_bulk_records, insert_bulk_records, process_complete_records_ofac
from utils.export_excel import export_incomplete_results_excel


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
    masivo, completos = split_bulk_records(persons)

    # Paso 5: Insertar resultados masivos
    insert_bulk_records(masivo) 

    # Paso 6: Procesar registros completos en OFAC
    process_complete_records_ofac(completos)

    # Paso 7: Obtener resultados finales
    get_results()

    # Paso 8: Exportar resultados con información incompleta a Excel
    export_incomplete_results_excel() 

    # Paso 9: Limpiar resultados para próximas pruebas
    delete_results()

   
   

 

