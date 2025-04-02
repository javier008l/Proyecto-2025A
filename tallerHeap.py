def max_heapify(A, i, heap_size):
    """
    Función para mantener la propiedad de max-heap en un subárbol con raíz en el índice i.
    
    Parámetros:
    - A: Lista que representa el heap.
    - i: Índice del nodo actual.
    - heap_size: Tamaño actual del heap (puede ser menor que la longitud de A).
    """
    l = 2 * i + 1  # Índice del hijo izquierdo (LEFT)
    r = 2 * i + 2  # Índice del hijo derecho (RIGHT)
    
    # Comparar el nodo actual con su hijo izquierdo
    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    
    # Comparar el nodo actual (o el hijo izquierdo) con su hijo derecho
    if r < heap_size and A[r] > A[largest]:
        largest = r
    
    # Si el mayor no es el nodo actual, intercambiar y continuar heapificando
    if largest != i:
        A[i], A[largest] = A[largest], A[i]  # Intercambiar
        max_heapify(A, largest, heap_size)   # Llamada recursiva


def build_max_heap(A):
    """
    Función para construir un max-heap a partir de un arreglo.
    
    Parámetros:
    - A: Lista que representa el arreglo.
    """
    heap_size = len(A)
    # Empezar desde el último nodo que no es una hoja
    for i in range(heap_size // 2 - 1, -1, -1):
        max_heapify(A, i, heap_size)


def heap_sort(A):
    """
    Función para ordenar un arreglo utilizando el algoritmo HeapSort.
    
    Parámetros:
    - A: Lista que representa el arreglo.
    """
    heap_size = len(A)
    
    # Construir un max-heap
    build_max_heap(A)
    
    # Extraer elementos uno por uno
    for i in range(heap_size - 1, 0, -1):
        A[0], A[i] = A[i], A[0]  # Intercambiar el máximo (raíz) con el último elemento
        heap_size -= 1  # Reducir el tamaño del heap
        max_heapify(A, 0, heap_size)  # Restaurar la propiedad de max-heap


# Arreglo inicial
A = [4, 3, 8, 7, 5, 2, 6, 1]

print("Arreglo inicial:", A)

# Construir un max-heap
build_max_heap(A)
print("Arreglo después de Build-Max-Heap:", A)

# Ordenar el arreglo con HeapSort
heap_sort(A)
print("Arreglo después de HeapSort:", A)