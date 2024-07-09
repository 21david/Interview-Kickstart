from min_heap import MinHeap

# Small test
heap = MinHeap()

for i in [5, 8, 9, 2, 3, 1, 0, 8, 3]:
    heap.add(i)
    print(i, heap.arr)
    
print('--')
for i in range(7):
    ext = heap.extract()
    print(ext, heap.arr)
