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

def datos_clima(datos):
    elementos = {}
    archivo = open(datos, "r")
    for linea in archivo:
        linea = linea.strip()
        if linea != "":
            auxiliar = linea.split(";")
            if len(auxiliar) == 10:
                ciudad = auxiliar[0].strip()
                sensacion_t = auxiliar[6].strip()
                if sensacion_t == "No se calcula":
                    st = "No se calcula"
                else: 
                    st = float(sensacion_t)
                direccion_v, velocidad_v = viento(auxiliar[8])
                fcha_hra = fecha_hora(auxiliar[1], auxiliar[2])
                elementos[ciudad] = {
                    "fecha_hora": fcha_hra,
                    "estado": auxiliar[3].strip(),
                    "visibilidad": auxiliar[4].strip(),
                    "temperatura": float(auxiliar[5].strip()),
                    "sensacion_termica": st,
                    "humedad": auxiliar[7].strip(),
                    "direccion_viento": direccion_v,
                    "velocidad_viento": velocidad_v,
                    "presion": auxiliar[9].strip()
                }
    archivo.close()
    return elementos 
def cantidad_ciudades(observaciones):
    return len(observaciones)
def cantidad_ciudades_totales (observaciones):
    contador = 0
    for ciudades in observaciones:
        datos_ciudades = observaciones[ciudades]
        if datos_ciudades ["sensacion_termica"] != "No se calcula":
            contador = contador +1
    return contador