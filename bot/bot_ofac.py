from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os
import time


# Función para iniciar el driver de Selenium
def start_driver():
    # Configuración de Edge
    options = webdriver.EdgeOptions()
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    # Reemplaza con la ruta correcta de tu driver
    driver_path = r"C:\seleniumdriver\msedgedriver.exe"
    # Iniciar Edge
    service = Service(driver_path)
    driver = webdriver.Edge(service=service, options=options)
    return driver

def search_person(driver, nombre, direccion=None, pais=None):
    driver.get("https://sanctionssearch.ofac.treas.gov/")  
    time.sleep(2)  # Espera inicial

    # Nombre
    driver.find_element(By.ID, "ctl00_MainContent_txtLastName").send_keys(nombre)

    # Dirección
    if direccion:
        driver.find_element(By.ID, "ctl00_MainContent_txtAddress").send_keys(direccion)

    # País / Country (Select)
    if pais:
        select_country = Select(driver.find_element(By.ID, "ctl00_MainContent_ddlCountry"))
        try:
            select_country.select_by_visible_text(pais)
        except:
            # Si no encuentra el país, se deja "All"
            select_country.select_by_visible_text("All")

    # Botón Search
    driver.find_element(By.ID, "ctl00_MainContent_btnSearch").click()

    # Esperar a que aparezca el span de resultados
    try:
        lbl_result = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "ctl00_MainContent_lblResults"))
        )
        resultado_text = lbl_result.text  # Ej: "Lookup Results: 1 found"
        cantidad = int(''.join(filter(str.isdigit, resultado_text)))
    except:
        cantidad = 0

    return cantidad


# Guarda screenshot en carpeta local con formato: screenshots/fecha_idPersona.png
def guardar_screenshot(driver, idPersona):
    os.makedirs("screenshots", exist_ok=True)
    fecha = datetime.now().strftime("%Y%m%d")
    driver.save_screenshot(f"screenshots/{fecha}_{idPersona}.png")