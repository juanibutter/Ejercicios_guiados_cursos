print("=================================")
print("<<<SISTEMA VACACIONAL DE RAPPI>>>")
print("=================================")
print("")
nombre=input("Nombre del empleado: \n")
clave=int(input("""Área a la cual pertenece (1-2-3):
1.Dep. de Atención al cliente
2.Dep. de Logística
3.Gerencia \n"""))
antigüedad=float(input("Años de antigüedad en la empresa: "))
print("")
#clave1
if clave==1:
    if antigüedad>=1 and antigüedad<2:
        print("A",nombre,"le corresponden 6 días de vacaciones.")
    elif antigüedad>=2 and antigüedad<7:
        print("A",nombre,"le corresponden 14 días de vacaciones.")
    elif antigüedad>=7:
        print("A",nombre,"le corresponden 20 días de vacaciones.")
    else:
        print("A",nombre,"no le corresponden vacaciones.")
#clave2
elif clave==2:
    if antigüedad==1 and antigüedad<2:
        print("A",nombre,"le corresponden 7 días de vacaciones.")
    elif antigüedad>=2 and antigüedad<7:
        print("A",nombre,"le corresponden 15 días de vacaciones.")
    elif antigüedad>=7:
        print("A",nombre,"le corresponden 22 días de vacaciones.")
    else:
        print("A",nombre,"no le corresponden vacaciones.")
#clave3
elif clave==3:
    if antigüedad==1 and antigüedad<2:
        print("A",nombre,"le corresponden 10 días de vacaciones.")
    elif antigüedad>=2 and antigüedad<7:
        print("A",nombre,"le corresponden 20 días de vacaciones.")
    elif antigüedad>=7:
        print("A",nombre,"le corresponden 30 días de vacaciones.")
    else:
        print("A",nombre,"no le corresponden vacaciones.")
else:
    print("Departamento no registrado.")
