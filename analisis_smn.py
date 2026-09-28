from funciones_smn import datos_clima, cantidad_ciudades, cantidad_ciudades_totales, top_ciudades
observaciones = datos_clima("datos/estado_tiempo20260917.txt")
print("Top 5 más cálidas:")
print(top_ciudades(observaciones, "temperatura", n=5, descendente=True))
print("\nTop 5 con más viento:")
print(top_ciudades(observaciones, "velocidad_viento", n=5, descendente=True))