def dibujar_arbolito(altura):
    for i in range(altura):
        # Espacios a la izquierda para centrar el árbol
        espacios = ' ' * (altura - i - 1)
        # Asteriscos para la fila actual
        asteriscos = '*' * (2 * i + 1)
        # Imprimir la fila completa
        print(espacios + asteriscos)
    # Base del árbol
    print(' ' * (altura - 1) + '|')

# Pedir al usuario la altura del árbol
altura = int(input("Introduce la altura del arbolito: "))
dibujar_arbolito(altura)