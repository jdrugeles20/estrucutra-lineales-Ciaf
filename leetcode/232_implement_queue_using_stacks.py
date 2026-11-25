class MyQueue:

    def __init__(self):
        self.pila_entrada = []
        self.pila_salida = []

    def push(self, x: int) -> None:
        self.pila_entrada.append(x)

    def pop(self) -> int:
        self.peek()
        return self.pila_salida.pop()

    def peek(self) -> int:
        if not self.pila_salida:
            while self.pila_entrada:
                self.pila_salida.append(self.pila_entrada.pop())
        return self.pila_salida[-1]

    def empty(self) -> bool:
        return not self.pila_entrada and not self.pila_salida
        

  ## simula una cola(FIFO) usando dos pilas(LIFO) (pila_entrada) y pila_salida) para invertir el orden de salida) para invertir el orden de salida.


  ## complejidad temporal: 0(1) Amortizado-La operacion push toma 0(1). Aunque pop y peek transfiere de pila_entrada a pila_salida en 0(n) cuando la pila de salida esta vacia, cada elemento  se mueve como maximo una vez en tooda su vida util, resultando en un costo promedio de 0(1)por operacion.

  ## complejidad espacila: 0(n)se requiere almacenar un total de n elementos distribuidos entre ambas pilas auxiliares##  
