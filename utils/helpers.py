
# Función para validar los datos de dirección y país
def data_validation(direccion, pais):
    if direccion is None and pais is None:
        return "No cruza con maestra"
    if not direccion or not pais:
        return "Información incompleta"
    return "OK"