def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    # Contar la frecuencia de cada palabra
    frecuencia = {}
    for palabra in data:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    # Encontrar la palabra con la frecuencia más alta
    max_frecuencia = 0
    palabra_max = None
    for palabra, count in frecuencia.items():
        if count > max_frecuencia:
            max_frecuencia = count
            palabra_max = palabra

    # Imprimir la palabra con la frecuencia más alta
    print(palabra_max)

if __name__ == "__main__":
    main()