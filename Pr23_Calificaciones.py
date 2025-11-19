#Angel Isaac Dominguez Espinoza
#3ªB Programacion 
#Hacer un programa que solicite el nombre del usuario y por medio de un ciclo sus
#tres calificaciones. Obtenga el promedio final y al final indicar si aprobo o reprobo 


Nom = str(input("escribe tu nombre"))
res=0
for i in range(1,4):
    cal=float(input("escribe tres calificaciones "))
    res=(cal+cal+cal)/3
print("",res)
if cal>= 6:
    print("Felicidades ",Nom,"Has aprobado ")
else:
    print("lo siento ",Nom,"has reprobado  ")