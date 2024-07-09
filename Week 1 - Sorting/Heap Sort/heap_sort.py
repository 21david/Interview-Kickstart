from min_heap import MinHeap

def heap_sort(arr):
    heap = MinHeap()
    for n in arr:
        heap.add(n)

    sorted = []
    while not heap.is_empty():
        sorted.append(heap.extract())

    return sorted

arr = [5, 1, 8, -9, 8, 7, 0, -4, 6, 2, 3, 1]
print(heap_sort(arr))
