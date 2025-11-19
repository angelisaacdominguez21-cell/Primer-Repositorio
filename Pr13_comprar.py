# 3ªB Programacion Matutino 
# Autor: Angel Isaac Dominguez Espinoza 
# lEER 2 NUMEROS: SI SON IGUALES QUE LOS MULTIPLIQUE, SI EL PRIMERO 
#ES MAYOR QUE LOS RESTES Y SI NO QUE LOS SUME

print("\n")
n1=int(input("escribe un numero"))
n2=int(input("escribe otro numero"))
if n1==2:
    m=n1*n2
    print("tu resultado es:",m)
elif n1>n2:
    r=n1-n2
    print("tu resultado es:",r)
else:
    s=n1+n2
    print("tu resultado es:",s)