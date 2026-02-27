from db.consultas import insert_results_bulk
from utils.helpers import data_validation

# Separa las personas en dos listas:
#  - masivos: los que tienen información incompleta o no cruza
# - completos: los que tienen info para búsquedas OFAC (no se usarán por ahora)
def separar_registros_masivos(personas):
    masivos = []
    completos = []

    for fila in personas:
        idPersona, nombrePersona, direccion, pais = fila
        estado = data_validation(direccion, pais)

        if estado in ("Información incompleta", "No cruza con maestra"):
            masivos.append((idPersona, nombrePersona, pais, 0, estado))
        else:
            completos.append((idPersona, nombrePersona, pais))

    return masivos, completos

# Inserta registros masivos en la tabla Resultadosuser4105
def insertar_masivos(masivos):
    if masivos:
        insert_results_bulk(masivos)
