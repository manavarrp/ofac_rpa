from db.consultas import insert_results_bulk
from utils.helpers import data_validation
from bot.bot_ofac import start_driver, search_person
from bot.screenshot import guardar_screenshot
from bot.screenshot import guardar_screenshot
from db.consultas import insert_results_bulk

# Separa las personas en dos listas:
#  - masivos: los que tienen información incompleta o no cruza
# - completos: los que tienen info para búsquedas OFAC (no se usarán por ahora)
def split_bulk_records(personas):
    masivos = []
    completos = []
    # Validar cada persona y clasificarla
    for fila in personas:
        idPersona, nombrePersona, direccion, pais = fila
        estado = data_validation(direccion, pais)

        if estado in ("Información incompleta", "No cruza con maestra"):
            masivos.append((idPersona, nombrePersona, pais, 0, estado))
        else:
            completos.append((idPersona, nombrePersona, direccion, pais))

    return masivos, completos

# Inserta registros masivos en la tabla Resultadosuser4105
def insert_bulk_records(masivos):
    if masivos:
        insert_results_bulk(masivos)

# Procesa los registros completos para búsquedas OFAC y guarda resultados en la base de datos
def process_complete_records_ofac(completos):
    # Si no hay registros completos, no se hace nada
    if not completos:
        print("No hay registros completos para procesar en OFAC.")
        return []
    # Iniciar driver de Selenium y procesar cada registro completo
    driver = start_driver()
    resultados_ofac = []
    # Iterar sobre los registros completos y realizar búsquedas en OFAC
    for idPersona, nombrePersona, direccion, pais in completos:
        try:
            cantidad = search_person(driver, nombrePersona, direccion, pais)
            if cantidad > 0:
                guardar_screenshot(driver, idPersona)
            resultados_ofac.append((idPersona, nombrePersona, pais, cantidad, "OK"))
        except Exception as e:
            print(f"Error buscando {nombrePersona}: {e}")
            resultados_ofac.append((idPersona, nombrePersona, pais, 0, "NOK"))
    # Cerrar driver al finalizar
    driver.quit()
    # Insertar resultados en la base de datos
    insert_results_bulk(resultados_ofac)
    print(f"{len(resultados_ofac)} registros procesados en OFAC e insertados.")
    return resultados_ofac