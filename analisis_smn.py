from funciones_smn import datos_clima
observaciones = datos_clima("datos/estado_tiempo20260917.txt")
print("Cantidad de ciudades leídas:", len(observaciones))
print("Datos de Azul:", observaciones.get("Azul"))