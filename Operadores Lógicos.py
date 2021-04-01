#Conjunción

print("Conjunción (AND)")

num_uno=int(input("Dame un número mayor a dos y menor a cinco: "))
if num_uno>2 and num_uno<5:
    print("El número ",num_uno, " cumple con la condición. \n")
else:
    print("El número ",num_uno," NO cumple con la condición \n")

#Disyunción
print("Disyunción (OR)")
palabra=input("Para cumplir con la condición escribe 'si' o 'yes': \n")

if palabra=="si" or palabra=="yes":
    print("La condición se ha cumplido \n")
else:
    print("La condición NO se ha cumplido \n")

#Negación

print("Negación (NOT)")

num_dos=int(input("Introduce un número igual a 5: "))
if not num_dos==5:
    print("El número es diferente a cinco y SI cumple la condición \n")
else:
    print("El número es igual a cinco y no cumple la condición \n")
