class Factura:
    def __init__(self, numero, monto):
        self.numero = numero
        self.monto = monto

class Cliente:
    def __init__(self, numero):
        self.numero = numero
        self.facturas = []

    def agregar_factura(self, numero, monto):
        factura = Factura(numero, monto)
        self.facturas.append(factura)

# Función para encontrar un cliente por su número
def encontrar_cliente(clientes, numero_cliente):
    for cliente in clientes:
        if cliente.numero == numero_cliente:
            return cliente
    return None

# Ejemplo de uso
clientes = []

# Agregar clientes
clientes.append(Cliente(1))
clientes.append(Cliente(2))

# Ingresar facturas para los clientes
numero_cliente = int(input("Ingrese el número de cliente: "))
cliente = encontrar_cliente(clientes, numero_cliente)

if cliente:
    while True:
        numero_factura = input("Ingrese el número de la factura (o 'fin' para terminar): ")
        if numero_factura == 'fin':
            break
        monto_factura = float(input("Ingrese el monto de la factura: "))
        cliente.agregar_factura(numero_factura, monto_factura)
else:
    print("El cliente no existe.")

# Mostrar las facturas de cada cliente
for cliente in clientes:
    print(f"Facturas para el cliente {cliente.numero}:")
    for factura in cliente.facturas:
        print(f"Número: {factura.numero}, Monto: {factura.monto}")
