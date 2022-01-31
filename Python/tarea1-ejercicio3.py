#Ejercicio 3
#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado. Además se nos pide el precio que se cobra por gramo, , y se nos mostrará el total de dinero que necesitamos para realizar el envío.
#Definición del problema: Tenemos payasos y muñecas que pesas 112 g y 75 g. Necesitamos saber el peso en g total del paquete dependiendo del total de payasos y muñecas. Una vez sepamos el peso necesitamos saber cuanto cuesta el gramo para mostrar el total del coste del paquete por peso en g.
#Análisis: 
#Datos de entrada: payasos, muñecas, pesopayasos, pesomuñecas, costegramo (real)
#Datos de salida: totalgramos, totalcoste (real)
#
#Diseño:
#-pedir número de payasos y muñecas
#-calcular peso de payasos y muñecas multiplicando por 112 y 75
#-calcular y mostrar totalgramos
#-sabiendo costegramo (ej:3 euros) calcular totalcoste=totalgramos*costegramo

payasos=float(input("Dime el número de payasos: "))

muñecas=float(input("Dime el número de muñecas: "))

coste_gramo=float(input("Dime cuanto vale el gramo en euros: "))

peso_payasos=payasos*112
peso_muñecas=muñecas*75

total_gramos=peso_payasos+peso_muñecas

total_coste=total_gramos+coste_gramo

print("El total de gramos es:" ,total_gramos ,"y cuesta" ,total_coste)

