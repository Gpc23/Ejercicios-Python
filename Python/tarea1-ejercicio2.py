#Ejercicio 2
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, e imprima por #pantalla la frase “Tu índice de masa corporal es…” y el resultado.
#Definición del problema: Necesitamos saber el peso en kg y la estatura en metros para calcular el índice de masa corporal y almacenarlo en una variable.
#El índice de masa se calcula con el peso en kg dividido por la altura al cuadrado
#
#Análisis: 
#Datos de entrada: peso (kg) y estatura (m) (real)
#Datos de salida: índice de masa corporal (idmc)
#
#Diseño: 
#-pedir peso y altura en kg y m
#-calcular idmc con el p/(m)`2
#-escribir idmc con la frase enunciado

peso=float(input("Dime tu peso: "))
altura=float(input("Dime tu altura: "))

idmc=peso/(altura**2)

print("Tu indice de masa corporal es de: " ,idmc)