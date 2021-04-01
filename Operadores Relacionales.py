print("Introduce dos números a comparar \n")
num_uno=int(input("Introduce un número: "))
num_dos=int(input("Introduce otro número: "))
print("")
print("Los números a comparar son:",num_uno ,"y", num_dos)
if num_uno>num_dos:
    print("Es mayor...")
if num_uno>=num_dos:
    print("Es mayor o igual...")
if num_uno!=num_dos:
    print("Es diferente...")
if num_uno==num_dos:
    print("Es igual a...")
if num_uno<num_dos:
    print("Es menor...")
if num_uno<=num_dos:
    print("Es menor o igual...")
