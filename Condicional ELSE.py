print("Sistema para calcular el promedio de un alumno:")
nombre=input("Para comenzar, ¿Cual es tu nombre? ")
nota_uno=float(input(nombre+ " ¿Cuál es tu nota de Economía? "))
nota_dos=float(input(nombre+ " ¿Cuál es tu nota de Programación? "))
nota_tres=float(input(nombre+ " ¿Cuál es tu nota de Educación Física? "))
nota_cuatro=float(input(nombre+ " ¿Cuál es tu nota de Administración? "))
nota_cinco=float(input(nombre+ " ¿Cuál es tu nota de Derecho? "))
promedio=(nota_uno+nota_dos+nota_tres+nota_cuatro+nota_cinco)/5
if promedio>=6:
    print('Felicidades '+nombre+' ¡aprobaste! con un promedio de '+str(round(promedio,1)))
else:
    print("Lo lamento "+nombre+", no aprobaste, tu promedio fue de ", round(promedio,1))
print("Fin.")
