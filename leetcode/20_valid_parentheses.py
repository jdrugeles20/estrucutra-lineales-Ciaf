class Solution:
    def isValid(self, s: str) -> bool:
        pila = []
        pares = {")": "(", "]": "[", "}": "{"}

        for caracter in s:
            if caracter in pares:
                tope = pila.pop() if pila else "#"
                if pares[caracter] != tope:
                    return False
            else:
                pila.append(caracter)

        return len(pila) == 0


### complejidad temporal; O(N) el ciclo for recorre la cadena s de longitud n una unica vez. Dentro del cilco, las operaciones append(), pop() y la consulta en el diccionario pares se ejecutan en tiempo constante O(1).###

### COMPLEJIDAD ESPACIAL; En el peor caso (cuando todos los caracteres son de apertura, como ((())))) la pila almacena los n caracteres en memoria.
