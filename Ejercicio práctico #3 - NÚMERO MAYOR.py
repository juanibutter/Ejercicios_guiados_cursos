print("#######################################################")
print("#### PROGRAMA PARA DETERMINAR EL NÚMERO MÁS GRANDE ####")
print("####################################################### \n")

num_uno=int(input("Dame un número entero: "))
num_dos=int(input("Dame otro número entero: "))
num_tres=int(input("Dame un último número entero: "))

print("")

if num_uno>num_dos and num_uno>num_tres:
    print("El número",num_uno,"es el más grande.")
elif num_dos>num_tres:
    print("El número",num_dos,"es el más grande.")
else:
    print("El número",num_tres,"es el más grande.")

