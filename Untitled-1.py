import random
import copy


#creo lista
def creolista():
    lista=[]
    x=int(input("ingrese el largo de la lista= "))
    for i in range (x):
        lista.append(random.randint(50,780))
    return lista


#ordeno de menor a mayor
def ordenolista(a):
    desordenado=True
    while desordenado:
        desordenado=False
        for i in range (len(a)-1):
            if a[i]>a[i+1]:
                aux=a[i]
                a[i]=a[i+1]
                a[i+1]=aux
                desordenado=True
    return (a)    
            
#busqueda binaria
def buscopos(v,dato):
    izq=0
    der=len(v)-1
    pos=-1
    while izq<=der and pos==-1:
        centro=(izq+der)//2
        if v[centro]==dato:
            pos=centro
        elif v[centro]<dato:
            izq=centro+1
        else:
            der=centro-1
    return pos
            
#obtener minimo
def obtenerminimo(a):
    minimo=a[0]
    for i in range(len(a)-1):
        if a[i]<minimo:
            minimo=a[i]
    return minimo
    
        
#eliminar minimo
def eliminarminimo(a,b):
    minimo=b
    i=0
    while i<len(a):
        if a[i]==minimo:
            del a[i]
        i=i+1
    return a
        

a=creolista()
print(a)
print()

b=ordenolista(a)
print(b)
print()

c=int(input("ingrese numero a buscar posicion= "))
print()

d=buscopos(b,c)
if d==-1:
    print("no se encontro el valor")
else:
    print("la posision es: ",d)
    
    
e=obtenerminimo(a)

f=eliminarminimo(b,e)
print("el valor minimo es: ",e,"y la lista sin el minimo queda:",f,)
