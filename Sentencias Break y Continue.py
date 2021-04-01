#Break y Continue
#break

print("""
***********************
*** While con break ***
***********************\n""")

contador = 0
while contador < 10:
    contador += 1
    if contador == 5:
        break
    print("Valor actual de la variable:", contador)
print("Fin del programa, la sentencia break se ha ejecutado correctamente.")

#continue

print("""\n
**************************
*** While con continue ***
**************************\n""")

contador = 0
while contador < 10:
    contador += 1
    if contador == 5:
        continue
    print("Valor actual de la variable:", contador)
print("Fin del programa, la sentencia continue se ha ejecutado correctamente.")
