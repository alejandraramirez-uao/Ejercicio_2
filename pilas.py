# -*- coding: utf-8 -*-
# Parte A — Pilas

# TODO 1: Validación de paréntesis con pila
def balanceado(exp):
    pila = []
    pares = {')': '(', ']': '[', '}': '{'}

    for caracter in exp:
        if caracter in "([{":
            pila.append(caracter)
        elif caracter in ")]}":
            if not pila or pila.pop() != pares[caracter]:
                return False

    return len(pila) == 0


# TODO 2: Conversión de decimal a binario usando pila
def decimal_a_binario(n):
    pila = []

    if n == 0:
        return "0"

    while n > 0:
        residuo = n % 2
        pila.append(residuo)
        n = n // 2

    binario = ""
    while pila:
        binario += str(pila.pop())

    return binario


if __name__ == "__main__":
    print("== Pilas ==")
    print("Paréntesis balanceados:")
    print(balanceado("(a+b)*[c-d]"))   # True
    print(balanceado("(a+b*[c-d]"))    # False

    print("\nDecimal a binario:")
    print(decimal_a_binario(13))  # 1101
