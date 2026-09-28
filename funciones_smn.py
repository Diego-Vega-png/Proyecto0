from datetime import date, time, datetime, timedelta
def viento(cantidad_viento):
    if not cantidad_viento or cantidad_viento.strip().lower() == "sin_viento":
        return "sin_viento", 0.0
    lugares = cantidad_viento.strip().split()
    if len(lugares) >= 2:
        ubicaciones = " ".join(lugares[:-1])
        kms = float(lugares[-1])
        return ubicaciones, kms
    else:
        return cantidad_viento, 0.0
def fecha_hora(fecha, hora):
    datos_limpios = fecha.strip().replace("septiembre", "09")
    texto = datos_limpios + " " + hora.strip() 
    return datetime.strptime(texto, "%d-%m-%Y %H:%M")
