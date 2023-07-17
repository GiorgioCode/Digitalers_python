def bubble_sort(arr):
    n = len(arr)

    # Recorre todos los elementos del arreglo
    for i in range(n - 1):

        # Realiza el intercambio de elementos adyacentes si están en el orden incorrecto
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 456, 33, 12, 18, 20, 11, 90]
print("Arreglo desordenado:")
print(arr)
sorted_arr = bubble_sort(arr)
print("Arreglo ordenado:")
print(sorted_arr)
