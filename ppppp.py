import random
from collections import namedtuple
import numpy as np

# Estructura de datos
Pedido = namedtuple('Pedido', ['cliente', 'producto', 'cantidad', 'precio', 'estado'])

def generar_pedidos_completos(n=20):
    catalogo = {
        'Laptop': 15000, 'Monitor': 4000, 'Teclado': 800,
        'Mouse': 250, 'USB': 100, 'Webcam': 1200, 'Audifonos': 700
    }
    nombres = ['Juan Perez', 'Maria Lopez', 'Martin Perez', 'Pedro Gil', 'Ana Ruiz', 'Ricardo Sosa','Julian Olguin','Leonardo Ventura']
    estados = ['pagado', 'pendiente', 'cancelado']
    
    lista_pedidos = []
    for _ in range(n):
        producto_random = random.choice(list(catalogo.keys()))
        nuevo_p = Pedido(
            cliente=random.choice(nombres),
            producto=producto_random,
            cantidad=random.randint(1, 10),
            precio=catalogo[producto_random],
            estado=random.choice(estados)
        )
        lista_pedidos.append(nuevo_p)
    return lista_pedidos

def menu_pedidos():
    # Generamos datos iniciales
    data = generar_pedidos_completos(25)
    pedidos_np = np.empty(len(data), dtype=object)
    pedidos_np[:] = data
    
    while True:
        print("\n" + "="*30)
        print("  SISTEMA DE GESTIÓN DE PEDIDOS  ")
        print("="*30)
        print("1. Mostrar pedidos PAGADOS")
        print("2. Mostrar totales generales")
        print("3. Consultar pedidos por CLIENTE")
        print("4. Filtrar pedidos de ALTO VALOR (Lambda)")
        print("5. Salir")
        
        opcion = input("\nSelecciona una opción: ")

        if opcion == '1':
            # Uso de comprensión de listas (similar a lógica lambda)
            pagados = pedidos_np[[p.estado == 'pagado' for p in pedidos_np]]
            print(f"\n{'CLIENTE':<18} | {'PRODUCTO':<10} | {'ESTADO':<10}")
            print("-" * 45)
            for p in pagados:
                print(f"{p.cliente:<18} | {p.producto:<10} | {p.estado:<10}")
            print(f"\nTotal pagados: {len(pagados)}")

        elif opcion == '2':
            total_pedidos = len(pedidos_np)
            # Lambda para calcular el total de cada pedido individualmente
            monto_total = sum(map(lambda p: p.cantidad * p.precio, pedidos_np))
            print(f"\nResumen Financiero:")
            print(f"- Pedidos registrados: {total_pedidos}")
            print(f"- Ingreso total: ${monto_total:,.2f}")

        elif opcion == '3':
            # Consultoría por cliente integrada en el menú
            cliente_buscado = input("\nNombre del cliente a buscar: ").strip().lower()
            # Filtramos usando una función lambda dentro de filter()
            resultados = list(filter(lambda p: cliente_buscado in p.cliente.lower(), pedidos_np))
            
            if resultados:
                print(f"\nHistorial de {cliente_buscado.upper()}:")
                for r in resultados:
                    print(f"- {r.producto} ({r.cantidad} ud.): {r.estado}")
            else:
                print("No se encontró al cliente.")

        elif opcion == '4':
            # Lógica de Inferencia/Filtrado con Lambda
            # Filtramos pedidos cuyo valor total (cant * precio) sea mayor a $5,000
            umbral = 5000
            alto_valor = list(filter(lambda p: (p.cantidad * p.precio) > umbral, pedidos_np))
            
            print(f"\n--- PEDIDOS DE ALTO VALOR (> ${umbral}) ---")
            for p in alto_valor:
                total = p.cantidad * p.precio
                print(f"{p.cliente:<18} | {p.producto:<10} | Total: ${total:>8,.2f}")
            print(f"Se encontraron {len(alto_valor)} pedidos importantes.")

        elif opcion == '5':
            print("Cerrando sistema...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu_pedidos()