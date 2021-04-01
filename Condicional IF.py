print("Sistema para calcular el promedio de un alumno:")
nombre=input("Para comenzar, ¿Cual es tu nombre? ")
nota_uno=float(input(nombre+ " ¿Cuál es tu nota de Economía? "))
nota_dos=float(input(nombre+ " ¿Cuál es tu nota de Programación? "))
nota_tres=float(input(nombre+ " ¿Cuál es tu nota de Educación Física? "))
promedio=(nota_uno+nota_dos+nota_tres)/3
if promedio>=6:
    print('Felicidades '+nombre+' ¡aprobaste! con un promedio de '+str(promedio))
else:
    print("Lo lamento, "+nombre+" no aprobaste, tu promedio fue de", promedio)
print("Fin.")
