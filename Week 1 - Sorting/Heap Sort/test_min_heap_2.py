from min_heap import MinHeap
import random

# LARGE TEST
NUM_TESTS = 10000
def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i+1] < arr[i]:
            return False
    return True

print('starting large test...')
heap = MinHeap()
unsorted = 0
for _ in range(NUM_TESTS):
    heap.clear()

    # Add random numbers
    for i in range(random.randint(0, 50)):
        heap.add(0 if random.randint(0,9) == 0 else random.randint(-50, 50))

    # Extract all, should extract in order of least to greatest
    result_arr = []
    for i in range(len(heap.arr)):
        ext = heap.extract()
        result_arr.append(ext)

    bool = is_sorted(result_arr)
    if not bool:
        unsorted += 1
        print('not sorted!', result_arr)

print(' ...done. ', end='')
if unsorted:
    print(f'found {unsorted} failed test case(s).')
else:
    print(f'all {NUM_TESTS:,} test cases were correct.')
