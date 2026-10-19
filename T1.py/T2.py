"""
Problema 1: Laberinto con Backtracking
El raton parte de 'I' (esquina inferior izquierda) y debe llegar a 'F'
(esquina superior izquierda) acumulando 23 o mas puntos.
"""

PUNTAJE_MINIMO = 23

laberinto = [
    ['F', 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    ['I', 1, 3, 1, 0, 1, 1, 1, 1]
]

FILAS = 9
COLUMNAS = 9

# Orden de movimientos: arriba, derecha, abajo, izquierda
MOVIMIENTOS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

INICIO = (8, 0)   # casilla I
LLEGADA = (0, 0)  # casilla F


def valor_celda(fila, col):
    """Devuelve los puntos de una celda ('I' y 'F' equivalen a 1)."""
    celda = laberinto[fila][col]
    if celda == 'I' or celda == 'F':
        return 1
    return celda


def es_valido(fila, col, camino):
    """Verifica limites, que no sea obstaculo y que no este en el camino actual."""
    if fila < 0 or fila >= FILAS or col < 0 or col >= COLUMNAS:
        return False
    if laberinto[fila][col] == 0:
        return False
    if (fila, col) in camino:
        return False
    return True


def backtracking(fila, col, camino, puntaje):
    """
    Explora las alternativas desde (fila, col).
    Devuelve (camino, puntaje) si encuentra una solucion valida, o None.
    """
    # Se avanza a la celda actual
    camino.append((fila, col))
    puntaje += valor_celda(fila, col)

    # Caso base: llego a F
    if (fila, col) == LLEGADA:
        if puntaje >= PUNTAJE_MINIMO:
            return list(camino), puntaje
        # Puntaje insuficiente: se deshace y se prueba otra alternativa
        camino.pop()
        return None

    # Probar los movimientos en el orden: arriba, derecha, abajo, izquierda
    for df, dc in MOVIMIENTOS:
        nf, nc = fila + df, col + dc
        if es_valido(nf, nc, camino):
            resultado = backtracking(nf, nc, camino, puntaje)
            if resultado is not None:
                return resultado

    # Ninguna alternativa funciono: retroceder
    camino.pop()
    return None


def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(f"{str(x):>3}" for x in fila))


def construir_matriz_solucion(camino):
    """Marca el camino con '*' y conserva I, F y los obstaculos 0."""
    solucion = []
    for f in range(FILAS):
        fila_nueva = []
        for c in range(COLUMNAS):
            if (f, c) in camino and laberinto[f][c] not in ('I', 'F'):
                fila_nueva.append('*')
            elif laberinto[f][c] == 0:
                fila_nueva.append(0)
            elif laberinto[f][c] in ('I', 'F'):
                fila_nueva.append(laberinto[f][c])
            else:
                fila_nueva.append('.')  # celda libre que no forma parte del camino
            
        solucion.append(fila_nueva)
    return solucion


def main():
    print("=" * 50)
    print("PROBLEMA 1: LABERINTO CON BACKTRACKING")
    print("=" * 50)

    print("\nLaberinto original:\n")
    imprimir_matriz(laberinto)

    resultado = backtracking(INICIO[0], INICIO[1], [], 0)

    print()
    if resultado is not None:
        camino, puntaje = resultado
        print("Resultado: ¡El raton logro salir del laberinto!")
        print(f"Puntaje total del camino: {puntaje} (minimo requerido: {PUNTAJE_MINIMO})")
        print(f"Pasos del camino: {len(camino) - 1}")
        print("\nMatriz de salida ( * = camino, . = celda no usada, 0 = obstaculo ):\n")
        imprimir_matriz(construir_matriz_solucion(camino))
    else:
        print("Resultado: El raton NO logro salir del laberinto.")
        print(f"No existe un camino con {PUNTAJE_MINIMO} o mas puntos.")
        print("No se encontro una solucion.")


if __name__ == "__main__":
    main()