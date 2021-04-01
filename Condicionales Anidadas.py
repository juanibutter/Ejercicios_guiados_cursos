print("=========")
print("CONVERSOR")
print("========= \n")
print("Menú de opciones: \n")
print("Presiona 1 para convertir de número a palabra")
print("Presiona 2 para convertir de palabra a número \n")
opcion=int(input("¿Qué opción queres elegir? "))
print("")
if opcion==1:
    print("Conversor de número a palabra")
    numero=int(input("¿Qué número queres convertir? "))
    if numero==1:
        print("Uno")
    elif numero==2:
        print("Dos")
    elif numero==3:
        print("Tres")
    elif numero==4:
        print("Cuatro")
    elif numero==5:
        print("Cinco")
    else:
        print("Solo esta disponible del 1 al 5(inclusive)")
elif opcion==2:
    print("Conversor de palabra a número")
    palabra=str(input("¿Qué palabra queres convertir? "))
    palabra=palabra.lower()
    if palabra=="uno" or palabra=="Uno":
        print("1")
    elif palabra=="dos" or palabra=="Dos":
        print("2")
    elif palabra=="tres" or palabra=="Tres":
        print("3")
    elif palabra=="cuatro" or palabra=="Cuatro":
        print("4")
    elif palabra=="cinco" or palabra=="Cinco":
        print("5")
    else:
        print("Solo esta disponible del 'uno' al 'cinco'(inclusive) y con palabras bien escritas")
else:
    print("Opción no disponible")
print("Fin.")

