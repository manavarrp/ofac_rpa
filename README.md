# OFAC RPA Automation

Este proyecto automatiza la búsqueda de personas y entidades en la página de **OFAC Sanctions List**, valida datos en una base de datos **PostgreSQL**, toma capturas de pantalla de los resultados y genera un reporte en Excel para los registros con estado **"Información incompleta"**.

---

## Requisitos

* **Python 3.9+**
* **Microsoft Edge** (última versión)
* **WebDriver de Edge** (`msedgedriver.exe`)
  Ubicar el driver en `C:\seleniumdriver\` o ajustar la ruta en el código (`bot/bot_ofac.py`):

```python
driver_path = r"C:\seleniumdriver\msedgedriver.exe"
```


## Estructura del proyecto

project_root/
  ├── bot/
  │   ├── bot_ofac.py          # Inicio del driver y funciones de búsqueda
  │   ├── proceso_ofac.py      # Procesamiento de registros y screenshots
  │   └── screenshot.py        # Función guardar_screenshot
  ├── db/
  │   ├── conexion.py          # Conexión a PostgreSQL
  │   ├── consultas.py         # Consultas SQL
  │   └── validaciones.py      # Validaciones de datos
  ├── utils/
  │   ├── util.py              # Funciones utilitarias
  │   └── export_excel.py      # Función exportar Excel de incompletos
  ├── reports/                 # Carpeta donde se generan los reportes Excel
  ├── screenshots/             # Carpeta donde se guardan las capturas
  ├── main.py                  # Script principal de ejecución
  └── .env                     # Variables de entorno (URL de la base de datos)
## Configuración

1. Crear un archivo `.env` en la raíz del proyecto.
2. Configurar la URL de conexión a PostgreSQL:

```dotenv
DATABASE_URL=postgresql://usuario:password@host:puerto/nombre_base
```

3. Instalar dependencias

```bash
pip install selenium psycopg2-binary openpyxl python-dotenv
```

4. Verificar que `msedgedriver.exe` esté en la ruta configurada y que sea la misma versión del navegador Edge.
5. Ajustar cualquier path si es diferente.

## Uso

Desde la raíz del proyecto, ejecutar:

```bash
python main.py
```
