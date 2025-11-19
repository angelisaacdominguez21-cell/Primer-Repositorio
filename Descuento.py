#Angel Isaac Dominguez Espinoza
#3ªB Programacion 
#Por medio de un ciclo while hacer un programa que solicite el precio de cuatro articulos y al final 
#imprima el total a pagar por ellos considerando lo sigiente:si el total es mayor de $500 se le haraun 
#Descuento del 5% en caso contrario no tendra descuento 

i=0
res=0
while(i<4):
    precio=float(input("escribe el precio del articulo "))
    res=precio+res
    i+=1
if(res>500):
    res=res*0.5
    print("tendra un descuento del 5% por lo tanto pagara",res)
else:
    print("no tendra descuento por lo tanto pagara ",res)
