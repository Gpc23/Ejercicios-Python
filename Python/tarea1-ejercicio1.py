#Diseñar el algoritmo correspondiente a un programa que lea el valor correspondiente a una distancia en millas marinas y las escriba expresadas en metros.
#Definición del problema: Debemos saber una distancia en millas y representarla en metros.
#1 milla son 1609,34 metros
#Análisis: 
#Datos de entrada: millas (real) 
#Datos de salida: metros (real)
#
#Diseño:
#-pedir número de millas recorridas (distancia)
#-convertir a metros multiplicando por 1609,34 
#-escribir metros


millas = float(input("Dime las millas recorridas: "))

metros = millas * 1609.34

print("Los metros totales recorridos son:" ,metros ,"m")