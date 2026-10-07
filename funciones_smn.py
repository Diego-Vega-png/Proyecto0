from datetime import date, time, datetime, timedelta
def viento(cantidad_viento):
    dato_viento = cantidad_viento.strip()
    if not dato_viento or dato_viento.lower() == "calma":
        return "calma", 0.0
    
    lugares = dato_viento.split()
    if len(lugares) >= 2:
        ubicaciones = " ".join(lugares[:-1])
        kms = float(lugares[-1])
        return ubicaciones, kms
    else:
        return cantidad_viento, 0.0
def fecha_hora(fecha, hora):
    meses = {
        "enero":"01", "febrero":"02", "marzo":"03" , "abril":"04", "mayo":"05", "junio":"06", "julio":"07", "agosto":"08", "septiembre":"09",
        "octubre":"10", "noviembre":"11", "diciembre":"12"
    }
    datos_limpios = fecha.strip().lower()
    for mes_nombre, mes_numero in meses.items():
        if mes_nombre in datos_limpios:
            datos_limpios = datos_limpios.replace(mes_nombre,mes_numero)
            break
    texto = datos_limpios + " " + hora.strip() 
    return datetime.strptime(texto, "%d-%m-%Y %H:%M")

def datos_clima(datos):
    elementos = {}
    lineas_descartadas = 0
    archivo = open(datos, "r")
    for linea in archivo:
        linea = linea.strip()
        if linea != "":
            auxiliar = linea.split(";")
            if len(auxiliar) == 10:
                ciudad = auxiliar[0].strip()
                
                sensacion_t = auxiliar[6].strip()
                if sensacion_t == "No se calcula":
                    st = None
                else: 
                    st = float(sensacion_t)
                
                direccion_v, velocidad_v = viento(auxiliar[8])
                fcha_hra = fecha_hora(auxiliar[1], auxiliar[2])
                humedad_limpia = auxiliar[7].strip().replace("/","").strip()
                presion_limpia = auxiliar[9].strip().replace("/","").strip()
                elementos[ciudad] = {
                    "fecha_hora": fcha_hra,
                    "estado": auxiliar[3].strip(),
                    "visibilidad": auxiliar[4].strip(),
                    "temperatura": float(auxiliar[5].strip()),
                    "sensacion_termica": st,
                    "humedad": float(humedad_limpia) if humedad_limpia else None,
                    "direccion_viento": direccion_v,
                    "velocidad_viento": velocidad_v,
                    "presion": float(presion_limpia) if presion_limpia else None
                }
            else: 
                lineas_descartadas +=1    
    archivo.close()
    return elementos,lineas_descartadas
def obtener_valor(tupla):
    return tupla[1]
def cantidad_ciudades(observaciones):
    return len(observaciones)
def cantidad_ciudades_totales (observaciones):
   return len(observaciones)
def top_ciudades (observaciones,lugares,n=5, descendente=True ):
    ciudades_correctas = []
    for ciudad in observaciones:
        datos_ciudad = observaciones[ciudad]
        valor = datos_ciudad[lugares]
        if valor is not None and valor != "No se calcula":
            ciudades_correctas.append((ciudad,valor))
    ciudades_ordenadas = sorted(ciudades_correctas, key=obtener_valor, reverse=descendente)
    return ciudades_ordenadas[:n]