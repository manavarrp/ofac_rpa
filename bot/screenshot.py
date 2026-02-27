from datetime import datetime
import os

# Función para guardar screenshot con formato AAAAMMDD_idPersona.png
def guardar_screenshot(driver, idPersona):
    os.makedirs("screenshots", exist_ok=True)
    fecha = datetime.now().strftime("%Y%m%d")  # AAAAMMDD
    driver.save_screenshot(f"screenshots/{fecha}_{idPersona}.png")