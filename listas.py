# -*- coding: utf-8 -*-
# Parte C — Listas Enlazadas

# Nodo para lista simple
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# TODO 5: Lista enlazada simple
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        nuevo = Node(data)
        nuevo.next = self.head
        self.head = nuevo

    def insert_end(self, data):
        nuevo = Node(data)

        if self.head is None:
            self.head = nuevo
            return

        actual = self.head
        while actual.next:
            actual = actual.next

        actual.next = nuevo

    def traverse(self):
        actual = self.head
        while actual:
            print(actual.data)
            actual = actual.next

# Nodo para lista doblemente enlazada
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# TODO 6: Lista doblemente enlazada
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        nuevo = DNode(data)
        if self.head:
            self.head.prev = nuevo
            nuevo.next = self.head
        self.head = nuevo

    def insert_end(self, data):
        nuevo = DNode(data)

        if self.head is None:
            self.head = nuevo
            return

        actual = self.head
        while actual.next:
            actual = actual.next

        actual.next = nuevo
        nuevo.prev = actual

    def traverse_forward(self):
        actual = self.head
        while actual:
            print(actual.data)
            actual = actual.next

    def traverse_backward(self):
        actual = self.head

        if actual is None:
            return

        # ir al final
        while actual.next:
            actual = actual.next

        # recorrer hacia atrás
        while actual:
            print(actual.data)
            actual = actual.prev

if __name__ == "__main__":
    print("== Listas Enlazadas ==")

    print("\nLista simple:")
    l = LinkedList()
    l.insert_front(10)
    l.insert_end(20)
    l.traverse()

    print("\nLista doblemente enlazada:")
    dl = DoublyLinkedList()
    dl.insert_front(1)
    dl.insert_end(2)
    dl.insert_end(3)
    dl.traverse_forward()
    dl.traverse_backward()
