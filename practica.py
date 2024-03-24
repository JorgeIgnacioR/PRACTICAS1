
x=int(input("ingrese cantidad de clientes"))
lista=[numero for  numero in range (1,x+1)]
print(lista)

i=0
while lista[i]<=x:
    i=i+1
    print("Cliente",i,)
    fac=int(input("cantidad facturas del cliente="))
    for fac in range(fac):
        num_fac=int(input("numero de factura="))
        




