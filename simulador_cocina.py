class colapedidosrestaurante:
    """ implementacion propia de una cola (fifo) para gestionar pedidos en cocina"""

    def __init__(self, capacidad_max):
        if capacidad_max <= 0:
            raise ValueError("La capacidad máxima debe ser mayor que cero.")
        self.capacidad_max = capacidad_max
        self.pedidos = []

    def esta_vacia(self):
        """Verifica si la cola está vacía."""
        return len(self.pedidos) == 0

    def esta_llena(self):
        return len(self.pedidos) >= self.capacidad_max

    def agregar_pedido(self, mesa,producto):
        if self .esta_llena():
            raise OverflowError(f"[OVERFLOW] Cocina saturada ({self.capacidad_max}/{self.capacidad_max} pedidos en curso). "
                f"No se puede recibir '{producto}' (Mesa {mesa})."
            )

        orden = f"[{mesa}] {producto}"
        self.pedidos.append(orden)
        return f"pedido registrado:-> {orden}"

    def despachar_pedido(self):
        """Dequeue: Entrega el pedido más antiguo que está al frente de la cola (O(n))."""
        if self.esta_vacia():
            raise IndexError("[UNDERFLOW] No hay pedidos pendientes por preparar en cocina.")
        return self.pedidos.pop(0)

    def consultar_siguiente(self):
        """Peek: Consulta el próximo pedido a preparar sin retirarlo (O(1))."""
        if self.esta_vacia():
            return "Cocina libre: no hay pedidos en cola."
        return self.pedidos[0]

    def mostrar_estado(self):
        """Muestra la ocupación actual y el orden exacto de salida (Frente -> Final)."""
        ocupacion = f"{len(self.pedidos)}/{self.capacidad_max}"
        if self.esta_vacia():
            return f"Estado de Cocina [{ocupacion}]: Cola vacía."
        return f"Estado de Cocina [{ocupacion}] (Siguiente -> Último): {' | '.join(self.pedidos)}"

def iniciar_sistema():
    # CAMBIA ESTE VALOR POR EL NÚMERO DE LISTA DEL PRIMER INTEGRANTE ALFABÉTICAMENTE
    N = 8
    capacidad_max = (N % 4) + 3
    cocina = colapedidosrestaurante(capacidad_max)

    print(f"=== SISTEMA DE PEDIDOS EN COCINA (N={N} | Capacidad Máxima={capacidad_max}) ===")

    while True:
        print("\n1. Ingresar nuevo pedido (Enqueue)")
        print("2. Despachar/Entregar siguiente pedido (Dequeue)")
        print("3. Consultar próximo pedido a preparar (Peek)")
        print("4. Ver fila actual de pedidos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                mesa = input("Número de mesa: ").strip()
                producto = input("Nombre del plato o producto: ").strip()
                if not mesa or not producto:
                    print("[Error] La mesa y el producto son obligatorios.")
                    continue
                print(cocina.agregar_pedido(mesa, producto))
            elif opcion == "2":
                entregado = cocina.despachar_pedido()
                print(f"Pedido despachado -> {entregado}")
            elif opcion == "3":
                print(f"Próximo pedido en turno: {cocina.consultar_siguiente()}")
            elif opcion == "4":
                print(cocina.mostrar_estado())
            elif opcion == "5":
                print("Cerrando sistema de cocina...")
                break
            else:
                print("Opción inválida. Ingrese un número del 1 al 5.")
        except (OverflowError, IndexError) as error:
            print(error)


if __name__ == "__main__":
    iniciar_sistema()
