
#Angel Isaac Dominguez Espinoza 
#3ªB Programacion T.M.
#Programa que realiza operaciones basicas con dos numeros 

numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("ingresa el segundo numero:"))
res = 0
print("\n")
print("Menu")
print("1. Suma")
print("2. Resta ")
print("3. Multiplicacion")
print("4. Dividir")
print("5. Salir")

opcion = input ("Elige una opcion: ")
if opcion == "1":
    res=numero1+numero2
    print("El resultado de la Suma es: ",res)
elif opcion == "2":
    res=numero1-numero2
    print("El resultado de la Resta es: ",res)
elif opcion == "3":
    res=numero1*numero2
    print("El resultado de la Multiplicacion es: ",res) 
elif opcion == "4":
        if(numero1>numero2):
            res=numero1/numero2
            print("El resultado de la Division  es: ",res)     
        else:
            print("No se puede realizar la operacion" )  
elif opcion == "5":
    print("Saliendo del programa.")
else:
    print("Obsion no valida.")