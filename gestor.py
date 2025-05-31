class MinHeap:
    """
    Implementación de MinHeap para cola de tareas con prioridad.
    Los valores de prioridad más bajos representan tareas con mayor prioridad (1 es la prioridad más alta).
    """
    def __init__(self):
        # Inicializa una lista vacía para almacenar el heap
        self.heap = []
        # Inicializa el contador de tamaño
        self.size = 0
    
    def parent_index(self, i):
        """Devuelve el índice del padre del elemento en el índice i"""
        return (i - 1) // 2
    
    def left_child_index(self, i):
        """Devuelve el índice del hijo izquierdo del elemento en el índice i"""
        return 2 * i + 1
    
    def right_child_index(self, i):
        """Devuelve el índice del hijo derecho del elemento en el índice i"""
        return 2 * i + 2
    
    def swap(self, i, j):
        """Intercambia los elementos en los índices i y j"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def is_leaf(self, i):
        """Verifica si el elemento en el índice i es un nodo hoja"""
        return (self.left_child_index(i) >= self.size) and (self.right_child_index(i) >= self.size)
    
    def insert(self, task):
        """
        Inserta una nueva tarea en el heap
        
        Args:
            task: Una tupla de (nombre, prioridad) donde nombre es un string y prioridad es un entero
        """
        # Verificar si el heap está en capacidad máxima (no implementado ya que usamos listas dinámicas)
        
        # Añadir la tarea al final del heap
        self.heap.append(task)
        current = self.size
        self.size += 1
        
        # Burbujeo hacia arriba: Comparar con el padre e intercambiar si es necesario
        while current > 0 and self.heap[current][1] < self.heap[self.parent_index(current)][1]:
            self.swap(current, self.parent_index(current))
            current = self.parent_index(current)
    
    def extract_min(self):
        """
        Extrae y devuelve la tarea con mayor prioridad (valor de prioridad más bajo)
        
        Returns:
            La tarea con mayor prioridad o None si el heap está vacío
        """
        if self.size == 0:
            return None
        
        # Obtener la tarea mínima (raíz)
        min_task = self.heap[0]
        
        # Mover el último elemento a la raíz y reducir el tamaño
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heap.pop()
        
        # Reorganizar el heap si no está vacío
        if self.size > 0:
            self.min_heapify(0)
        
        return min_task
    
    def min_heapify(self, i):
        """
        Mantiene la propiedad de min-heap comenzando desde el índice i
        
        Args:
            i: El índice desde donde comenzar la reorganización
        """
        if self.is_leaf(i):
            return
        
        # Encontrar índices de los hijos
        left = self.left_child_index(i)
        right = self.right_child_index(i)
        smallest = i
        
        # Verificar si existe el hijo izquierdo y tiene menor prioridad
        if left < self.size and self.heap[left][1] < self.heap[smallest][1]:
            smallest = left
        
        # Verificar si existe el hijo derecho y tiene menor prioridad
        if right < self.size and self.heap[right][1] < self.heap[smallest][1]:
            smallest = right
        
        # Si alguno de los hijos tiene menor prioridad, intercambiar y continuar reorganizando
        if smallest != i:
            self.swap(i, smallest)
            self.min_heapify(smallest)
    def print_heap(self):
        """Imprime el estado actual del heap"""
        if self.size == 0:
            print("El Heap está vacío")
            return
        
        print("Estado Actual del Heap:")
        print("------------------------")
        print("Índice | Nombre Tarea | Prioridad")
        print("------------------------")
        for i in range(self.size):
            print(f"{i:6d} | {self.heap[i][0]:12s} | {self.heap[i][1]}")
        print("------------------------")


# Uso del programa
if name == "main":
    # Crear una nueva cola de tareas con prioridad
    cola_tareas = MinHeap()
    
    print("=== GESTOR DE TAREAS CON PRIORIDAD ===")
    print("Ingrese 5 tareas con sus respectivas prioridades")
    print("(Recuerde: 1 es la prioridad más alta, números mayores indican menor prioridad)")
    print("")
        # Solicitar al usuario que ingrese 5 tareas
    for i in range(5):
        print(f"--- Tarea #{i+1} ---")
        nombre = input("Nombre de la tarea: ")
        
        # Validar que la prioridad sea un número entero
        while True:
            try:
                prioridad = int(input("Prioridad (número entero): "))
                break
            except ValueError:
                print("Error: Debe ingresar un número entero. Intente nuevamente.")
        
        # Insertar la tarea en el heap
        cola_tareas.insert((nombre, prioridad))
        print(f"Tarea '{nombre}' con prioridad {prioridad} insertada correctamente.\n")
    
    # Imprimir el estado del heap después de la inserción
    print("\nEstado del heap después de insertar todas las tareas:")
    cola_tareas.print_heap()
    
    # Extraer tareas en orden de prioridad
    print("\nExtrayendo tareas en orden de prioridad:")
    tareas_extraidas = []
    while cola_tareas.size > 0:
        tarea = cola_tareas.extract_min()
        tareas_extraidas.append(tarea)
        print(f"Extraída: '{tarea[0]}' con prioridad {tarea[1]}")
        print("Estado del heap después de la extracción:")
        cola_tareas.print_heap()
        print("")
    
    # Imprimir la lista final ordenada
    print("\nTareas en orden de prioridad:")
    for i, tarea in enumerate(tareas_extraidas):
        print(f"{i+1}. '{tarea[0]}' (Prioridad: {tarea[1]})")
