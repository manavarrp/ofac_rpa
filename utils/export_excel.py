import pandas as pd
import os
from db.consultas import get_results  # tu método que trae todos los resultados
from datetime import datetime

# Función para exportar resultados con información incompleta a Excel
def export_incomplete_results_excel():
    # Traer todos los resultados
    resultados = get_results()
    
    # Filtrar solo los que tengan estadoTransaccion = "Información incompleta"
    incompletos = [r for r in resultados if r[5] == "Información incompleta"]  # suponiendo que el campo está en la posición 5
    
    if not incompletos:
        print("No hay registros con estado 'Información incompleta'")
        return
    
    # Crear DataFrame para exportar
    df = pd.DataFrame(
        incompletos, 
        columns=["ID", "Persona ID", "Nombre", "País", "Cantidad de resultados", "Estado de transacción"]
    )
    
    # Crear carpeta reports si no existe
    os.makedirs("reports", exist_ok=True)
    
    # Guardar Excel con fecha
    fecha = datetime.now().strftime("%Y%m%d")
    file_path = f"reports/incomplete_results_{fecha}.xlsx"
    df.to_excel(file_path, index=False)
    print(f"Reporte generado: {file_path}")