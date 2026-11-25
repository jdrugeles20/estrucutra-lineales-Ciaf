# estructura-lineales-Ciaf
![Evidencia](capturasimulador.py.png,simulador,py2pruebasoverflow.png)
# Estructuras de Datos Lineales — Sistema de Gestión de Pedidos en Cocina (CIAF)

Proyecto académico desarrollado en **Python** para aplicar estructuras de datos lineales (**Cola / FIFO** y **Pila / LIFO**) en la resolución de problemas prácticos de flujo crítico y retos algorítmicos en **LeetCode**, evaluando su eficiencia temporal y espacial mediante notación **Big-O**.

---

## 1. Integrantes y Parametrización del Equipo ($N$ y $\text{capacidadMax}$)

Siguiendo la regla institucional, se ordenaron alfabéticamente por apellido los integrantes del equipo según el listado oficial de asistencia de **Estructura de Datos (Grupo Lunes)**:

| Orden Alfabético | Apellidos y Nombres | Número de Lista Oficial |
| :---: | :--- | :---: |
| **1 (Primer integrante)** | **Lopez Restrepo Juan Felipe** | **8** |
| **2** | Morales Romero David | 11 |
| **3** | Rugeles Oyola Juan David | 20 |

* **Parámetro $N$ obtenido:** `8` *(correspondiente al número de lista oficial del primer integrante en orden alfabético)*.
* **Cálculo de Capacidad Máxima ($\text{capacidadMax}$):**
  $$\text{capacidadMax} = (N \bmod 4) + 3 = (8 \bmod 4) + 3 = 0 + 3 = \mathbf{3}$$
* **Límite operativo del simulador:** La cola de pedidos en cocina soporta un máximo de **3 órdenes simultáneas** antes de disparar control de desbordamiento (**Overflow**).

---

## 2. Caso de Aplicación: Cola de Pedidos en Cocina de Restaurante (`simulador_pedidos.py`)

### Escenario y Justificación de la Estructura
* **Escenario elegido:** Gestión y despacho de órdenes de comida en la cocina de un restaurante.
* **Estructura seleccionada:** **Cola (FIFO — *First In, First Out*)**, implementada mediante una clase propia (`ColaPedidosRestaurante`) con capacidad acotada.
* **¿Por qué modela mejor el problema?** En una cocina, el orden de llegada de las comandas es crítico para la calidad del servicio: el primer pedido registrado por un mesero debe ser el primero en prepararse y despacharse. Una Cola garantiza equidad cronológica y evita que órdenes antiguas queden rezagadas o se entreguen frías.

### Operaciones Principales del Flujo
1. **Inserción (`agregar_pedido` / *Enqueue*):** Registra una nueva orden (mesa y plato) al **final** de la fila en tiempo constante $O(1)$. Si la ocupación alcanza `capacidadMax = 3`, bloquea la operación lanzando una excepción de desbordamiento (**Overflow**).
2. **Eliminación (`despachar_pedido` / *Dequeue*):** Retira y entrega el pedido ubicado al **frente** de la cola (el más antiguo en espera). Si no hay pedidos pendientes, controla el error mediante un mensaje de estructura vacía (**Underflow**).
3. **Consulta del elemento actual (`consultar_siguiente` / *Peek*):** Permite al cocinero visualizar el próximo pedido a preparar sin retirarlo de la fila ni alterar el orden de atención en $O(1)$.
4. **Monitoreo (`mostrar_estado`):** Muestra la ocupación actual (`[actual/3]`) y el orden exacto de salida desde el frente hasta el final en $O(n)$.
