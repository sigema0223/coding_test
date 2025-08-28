def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        swap(arr, i, largest)
        heapify(arr, n, largest)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        swap(arr, 0, i)
        heapify(arr, i, 0)

    return arr

def main():
    arr = [12, 11, 13, 5, 6, 7]
    print("Original array:", arr)
    sorted_arr = heap_sort(arr.copy())
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()