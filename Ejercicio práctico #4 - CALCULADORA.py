print("######################################")
print("### CALCULADORA CON VARIABLE ÚNICA ###")
print("######################################")
print("""
++++++++++++++++++++++++
+++ MENÚ DE OPCIONES +++
++++++++++++++++++++++++ \n
1) Suma
2) Resta
3) Multiplicación
4) División
5) División entera
6) Exponente
7) Módulo o Resto
""")
numero=int(input("Que opción eliges: "))

if numero==1:
    print("Elegiste Suma \n")
    numero=int(input("Introduce un número:"))
    numero+=int(input("Introduce otro número:"))
    print("El resultado de la suma es",numero)
elif numero==2:
    print("Elegiste Resta \n")
    numero=int(input("Introduce un número:"))
    numero-=int(input("Introduce otro número:"))
    print("El resultado de la resta es",numero)
elif numero==3:
    print("Elegiste Multiplicación \n")
    numero=int(input("Introduce un número:"))
    numero*=int(input("Introduce otro número:"))
    print("El resultado de la multiplicación es",numero)
elif numero==4:
    print("Elegiste División \n")
    numero=float(input("Introduce un número:"))
    numero/=float(input("Introduce otro número:"))
    print("El resultado de la división es",round(numero,2))
elif numero==5:
    print("Elegiste División entera \n")
    numero=float(input("Introduce un número:"))
    numero//=float(input("Introduce otro número:"))
    print("El resultado de la división entera es",numero)
elif numero==6:
    print("Elegiste Exponente \n")
    numero=int(input("Introduce un número:"))
    numero**=int(input("Introduce otro número:"))
    print("El resultado del exponente es",numero)
elif numero==7:
    print("Elegiste Módulo o Resto \n")
    numero=int(input("Introduce un número:"))
    numero%=int(input("Introduce otro número:"))
    print("El módulo o resto es",numero)
else:
    print("No hay más opciones disponibles.")
