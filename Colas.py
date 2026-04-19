# -*- coding: utf-8 -*-
# Parte B — Colas
from collections import deque
import heapq

# TODO 3: Simulación de turnos con cola
def simulacion_turnos(clientes):
    cola = deque()

    # encolar
    for cliente in clientes:
        cola.append(cliente)

    # desencolar
    while cola:
        cliente = cola.popleft()
        print("Atendiendo a:", cliente)

# TODO 4: Cola de prioridad de tareas con heapq
def cola_prioridad(tareas):
    heap = []

    # encolar con prioridad
    for tarea in tareas:
        heapq.heappush(heap, tarea)

    # desencolar por prioridad
    while heap:
        prioridad, nombre = heapq.heappop(heap)
        print("Atendiendo tarea:", nombre, "prioridad", prioridad)

if __name__ == "__main__":
    print("== Colas ==")
    print("Simulación de turnos:")
    simulacion_turnos(["Cliente1", "Cliente2", "Cliente3"])

    print("\nCola de prioridad:")
    cola_prioridad([(2,"tarea media"), (1,"tarea alta"), (3,"tarea baja")])
