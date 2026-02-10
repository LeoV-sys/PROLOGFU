from collections import namedtuple
from functools import reduce

# --- DEFINICIÓN DE DATOS (INMUTABLES) ---
# Usamos namedtuple para garantizar que los datos del pedido no cambien (Inmutabilidad)
Pedido = namedtuple('Pedido', ['cliente', 'producto', 'cantidad', 'precio', 'estado'])

# Base de conocimiento (Lista de pedidos)
# Se asume que esto es la entrada de datos del sistema 
pedidos_db = [
    Pedido('Juan Perez', 'Laptop', 1, 15000, 'pagado'),
    Pedido('Maria Lopez', 'Mouse', 2, 250, 'pendiente'),
    Pedido('Martin Perez', 'Teclado', 1, 800, 'pagado'),
    Pedido('Pedro Gil', 'Monitor', 2, 4000, 'cancelado'),
    Pedido('Ana Ruiz', 'USB', 5, 100, 'pagado')
]

# --- FUNCIONES PURAS Y LÓGICA ---

def calcular_monto_pedido(pedido):
    """
    Función pura que calcula el total de una sola línea de pedido.
    Regla: Cantidad * Precio
    """
    return pedido.cantidad * pedido.precio

# 1. USO DE RECURSIVIDAD 
# Objetivo: Calcular totales de pedidos 
def total_ventas_recursivo(lista_pedidos):
    """
    Calcula la suma total de todos los pedidos usando recursividad.
    Caso base: Si la lista está vacía, el total es 0.
    Caso recursivo: Valor del primer pedido + total del resto de la lista.
    """
    if not lista_pedidos:
        return 0
    else:
        cabeza = lista_pedidos[0]
        cola = lista_pedidos[1:]
        return calcular_monto_pedido(cabeza) + total_ventas_recursivo(cola)

# 2. USO DE FUNCIONES DE ORDEN SUPERIOR Y LAMBDAS 
# Objetivo: Identificar pedidos pagados 
def obtener_pedidos_pagados(lista_pedidos):
    """
    Usa 'filter' y una expresión 'lambda' para obtener solo los pagados.
    """
    # Lambda define la regla: el estado debe ser 'pagado'
    return list(filter(lambda p: p.estado == 'pagado', lista_pedidos))

# Objetivo: Consultar información por cliente 
def consultar_cliente(nombre, lista_pedidos):
    """
    Devuelve los pedidos de un cliente específico usando filter.
    """
    return list(filter(lambda p: p.cliente == nombre, lista_pedidos))

# 3. INFERENCIA DE INFORMACIÓN (REGLAS LÓGICAS) 
def inferir_pedido_vip(pedido):
    """
    Regla lógica: Un pedido es VIP si el monto supera los $10,000.
    """
    return calcular_monto_pedido(pedido) > 10000

def obtener_pedidos_vip(lista_pedidos):
    """
    Usa map y filter para inferir y extraer pedidos de alto valor.
    """
    return list(filter(inferir_pedido_vip, lista_pedidos))

# 4. USO DE REDUCE (Combinación de resultados)
def total_ventas_reduce(lista_pedidos):
    """
    Alternativa a la recursividad usando reduce (estilo funcional moderno).
    """
    return reduce(lambda acumulado, p: acumulado + calcular_monto_pedido(p), lista_pedidos, 0)

# --- EJECUCIÓN DEL CASO DE ESTUDIO ---

if __name__ == "__main__":
    print("--- SISTEMA DE GESTIÓN DE PEDIDOS (ENFOQUE FUNCIONAL) ---")
    
    # 1. Mostrar pedidos pagados
    pagados = obtener_pedidos_pagados(pedidos_db)
    print(f"\n1. Pedidos Pagados (Filter + Lambda): {len(pagados)}")
    for p in pagados:
        print(f"   - {p.cliente}: {p.producto} ({p.estado})")

    # 2. Calcular total de ventas (Recursivo)
    total_rec = total_ventas_recursivo(pedidos_db)
    print(f"\n2. Total de Ventas (Recursividad): ${total_rec}")

    # 3. Consultar cliente específico
    cliente_buscado = 'Juan Perez'
    pedidos_juan = consultar_cliente(cliente_buscado, pedidos_db)
    print(f"\n3. Pedidos de {cliente_buscado}:")
    for p in pedidos_juan:
        print(f"   - {p.producto} (Cant: {p.cantidad})")

    # 4. Inferir Pedidos VIP (Reglas Lógicas)
    vips = obtener_pedidos_vip(pedidos_db)
    print(f"\n4. Pedidos VIP inferidos (> $10,000):")
    for p in vips:
        print(f"   - {p.cliente} compró {p.producto} por ${calcular_monto_pedido(p)}")