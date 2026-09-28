from funciones_smn import datos_clima, cantidad_ciudades, cantidad_ciudades_totales
observaciones = datos_clima("datos/estado_tiempo20260917.txt")
print("Cantidad de ciudades leídas:", len(observaciones))
print("Datos de Azul:", observaciones.get("Azul"))
print("Total de ciudades:", cantidad_ciudades(observaciones))
print("Ciudades completas:", cantidad_ciudades_totales(observaciones))