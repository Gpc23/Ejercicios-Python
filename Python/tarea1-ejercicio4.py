#Ejercicio 4
#Diseñar el algoritmo correspondiente a un programa que pida el total de kilómetros recorridos, el precio de la gasolina (por litro), el consumo del coche (litros/100 #km) y nos muestre la siguiente información:
#    • El total de litros de gasolina que ha gastado en el trayecto.
#    • ¿Cuánto dinero te ha costado la gasolina?
#
#Definición del problema: Necesitamos saber el total de km, el precio de la gasolina por litro y el consumo para calcular el total de litros de gasolina dependiendo de #los km recorridos, y el dinero que ha costado suponiendo el total de litros gastados o consumidos
#Análisis:
#Datos de entrada: km, precio_gasolina, consumo 
#Datos de salida: precio_total, consumo_total
#Diseño:
#-pedir km, precio_gasolina, consumo (en litros)
#-calcular consumo_coche = consumo / 100
#-calcular consumo_total = consumo_coche / km
#-calcular precio_total =consumo_total(L) * precio_gasolina(€/L)
#-escribir consumo_total, precio_total

km=float(input("Dime el número de km recorridos: "))
precio_gasolina=float(input("Dime el precio de la gasolina en euros por litro: "))
consumo=float(input("Dime el consumo en litros: "))

consumo_coche=consumo/100
consumo_total=consumo_coche/km

precio_total=consumo_total*precio_gasolina

print("El consumo total en litros según los km recorridos es: " ,consumo_total ,"y el coste total segun los litros gastados en el consumo es de: " ,precio_total ,"euros")

