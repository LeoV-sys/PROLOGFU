import random
from collections import namedtuple

# Estructura de datos
Pedido = namedtuple('Pedido', ['cliente', 'producto', 'cantidad', 'precio', 'estado'])

def generar_pedidos_completos(n=20):
    """Genera pedidos con nombres, productos y precios vinculados."""
    
    # Catálogo de precios fijos
    catalogo = {
        'Laptop': 15000,
        'Monitor': 4000,
        'Teclado': 800,
        'Mouse': 250,
        'USB': 100,
        'Webcam': 1200,
        'Audifonos':700
    }
    
    nombres = ['Juan Perez', 'Maria Lopez', 'Martin Perez', 'Pedro Gil', 'Ana Ruiz', 'Ricardo Sosa','Julian Olguin','Leonardo Ventura']
    estados = ['pagado', 'pendiente', 'cancelado']
    
    lista_pedidos = []
    
    for _ in range(n):
        # Seleccionamos el producto y su precio correspondiente
        producto_random = random.choice(list(catalogo.keys()))
        precio_fijo = catalogo[producto_random]
        
        # Creamos el Pedido incluyendo el nombre del cliente
        nuevo_p = Pedido(
            cliente=random.choice(nombres),
            producto=producto_random,
            cantidad=random.randint(1, 10),
            precio=precio_fijo,
            estado=random.choice(estados)
        )
        lista_pedidos.append(nuevo_p)
        
    return lista_pedidos
