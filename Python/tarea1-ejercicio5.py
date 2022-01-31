#Ejercicio 5
#Suponiendo que una paella se puede cocinar exclusivamente con arroz y gambas, y que para cada cuatro personas se utiliza medio kilo de arroz 
# y un cuarto de kilo de gambas, escribir un programa que pida por pantalla el número de comensales para la paella, el precio por kilo de los 
# ingredientes y muestre las cantidades de los ingredientes necesarios y el coste de la misma.
#
#Definición del problema: Sabeos que una paella tiene arroz y gambas y que por cada 4 personas se gasta  ½ kilo de arroz y ¼ de gambas. 
# Hay que pedir el total de personas, el precio por kilo de arroz y gambas, y mostrar el total de kilos y el total del coste.
#
#Análisis:
#Datos de entrada: personas, precio_kilo_arroz, precio_kilo_gamba
#Datos de salida: total_kilos, total_coste
#
#Diseño:
#-pedir numero total de personas, precio_kilo_arroz, precio_kilo_gamba
#-calcular kilos de arroz=(personas*1/2)/4
#-calcular kilos de gamba=(personas*1/4)/4
#-calcular total de kilos
#-calcular coste total

personas=int(input("Dime el numero de personas que van a comer paella: "))
precio_kilo_arroz=float(input("Dime el coste del kilo de arroz: "))
precio_kilo_gamba=float(input("Dime el coste del kilo de gamba: "))

kilos_arroz=(personas*(1/2))/4
kilos_gamba=(personas*(1/4))/4

total_coste=(kilos_arroz*precio_kilo_arroz)+(kilos_gamba*precio_kilo_gamba)

print("El total de kilos de arroz que se han utilizado para la paella son:" ,kilos_arroz)
print("El total de kilos de gamba que se han utilizado para la paella son:" ,kilos_gamba)
print("El coste de la paella ha sido:" ,total_coste)