import sys
from funciones_smn import datos_clima, cantidad_ciudades, cantidad_ciudades_totales, top_ciudades
if len(sys.argv) < 2:
        print("Erro: debe elegir una ruta de archivo concreta")
        sys.exit(1)
archivo = sys.argv[1]
observaciones, linea_invalida = datos_clima(archivo)
if linea_invalida > 0:
        print (f"lineas descartadas: {linea_invalida} linea incompleta")
print(f"cantidad de ciudades procesadas: {cantidad_ciudades_totales(observaciones)}")

print("Top 5 más cálidas:")
for ciudad,temp in top_ciudades(observaciones,"temperatura", n=5, descendente=True):
    print(f"{ciudad}: {temp} c°")

print("top 5 mas frias:")
for ciudad,temp in top_ciudades(observaciones, "temperatura", n=5, descendente=False):
    print(f"{ciudad}: {temp} c°")

print("Top 5 con más viento:")
for ciudad,viento in top_ciudades(observaciones, "velocidad_viento", n=5, descendente=True):
      print(f"{ciudad}:{viento} km/h")

print("top 5 con menos viento")
for ciudad,viento in top_ciudades(observaciones, "velocidad_viento", n=5, descendente=False):
        print(f"{ciudad}:{viento} km/h")
